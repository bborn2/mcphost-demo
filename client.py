import asyncio
import json
import os
from typing import Optional
from contextlib import AsyncExitStack

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp.client.sse import sse_client

from openai import OpenAI

from dotenv import load_dotenv

load_dotenv()  # 从 .env 加载环境变量
api_key = os.getenv("DEEPSEEK_API_KEY")
amap_key = os.getenv("AMAP_KEY")

class MCPClient:
    def __init__(self):
        # 初始化会话和客户端对象
        self.session: Optional[ClientSession] = None
        self.exit_stack = AsyncExitStack()
        self.tools = None
         
        self.openai  = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

    async def connect_to_sse(self):
        sse_url = "https://mcp.amap.com/sse?key=amap_key"
        
        self._streams_context = sse_client(url=sse_url)
        streams = await self._streams_context.__aenter__()

        self._session_context = ClientSession(*streams)
        self.session: ClientSession = await self._session_context.__aenter__()

        # Initialize
        await self.session.initialize()

        # List available tools to verify connection
        print("Initialized SSE client...")
        print("Listing tools...")
        response = await self.session.list_tools()
        tools = response.tools
        print("\nConnected to server with tools:", [tool.name for tool in tools])

    async def connect_to_server(self, server_script_path: str):
        """连接到 MCP 服务器

        参数：
            server_script_path: 服务器脚本路径 (.py 或 .js)
        """
        is_python = server_script_path.endswith('.py')
        is_js = server_script_path.endswith('.js')
        if not (is_python or is_js):
            raise ValueError("服务器脚本必须是 .py 或 .js 文件")

        command = "python" if is_python else "node"
        server_params = StdioServerParameters(
            command=command,
            args=[server_script_path],
            env=None
        )

        stdio_transport = await self.exit_stack.enter_async_context(stdio_client(server_params))
        self.stdio, self.write = stdio_transport
        self.session = await self.exit_stack.enter_async_context(ClientSession(self.stdio, self.write))

        await self.session.initialize()

        # 列出可用工具
        response = await self.session.list_tools()
        tools = response.tools
        print("\n已连接到服务器，可用工具:", [tool.name for tool in tools])

    async def process_query(self, query: str) -> str:
        """使用 Claude 和可用工具处理查询"""
      
        messages = [{"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": query}]
 
        response = await self.session.list_tools()
        available_tools = [{
            "name": tool.name,
            "description": tool.description,
            "input_schema": tool.inputSchema
        } for tool in response.tools]

        tools = []
        for tool in available_tools:
            t = {}
            t["type"] = "function"
            t["function"] = tool
            t["function"]['parameters'] = t["function"]['input_schema']
            del t["function"]['input_schema']
            tools.append(t)
 
        response = self.openai.chat.completions.create(
            model="deepseek-chat",
            messages=messages,
            stream=False,
            tools=tools
        )
        # print(response)

        # 处理响应和工具调用
        tool_results = []
        final_text = []
        
        if len(response.choices[0].message.tool_calls) > 0:
            tool_name = response.choices[0].message.tool_calls[0].function.name
            tool_args = json.loads(response.choices[0].message.tool_calls[0].function.arguments)
            
            print(tool_name)
            print(tool_args)  

            assistant_message_content = []
        # for content in response.content:
        #     if content.type == 'text':
        #         final_text.append(content.text)
        #         assistant_message_content.append(content)
        #     elif content.type == 'tool_use':
        #         tool_name = content.name
        #         tool_args = content.input

                # 执行工具调用
            result = await self.session.call_tool(tool_name, tool_args)
            tool_results.append({"call": tool_name, "result": result})
            final_text.append(f"[调用工具 {tool_name}，参数 {tool_args}]")
            
            tool = response.choices[0].message.tool_calls[0]
            
            funcMessage = response.choices[0].message
            funcMessage.tool_calls = funcMessage.tool_calls[0:1]

            messages.append(funcMessage)
            messages.append({"role": "tool", "tool_call_id": tool.id, "content": result.content[0].text})
            
            # print(messages)
          
            response = self.openai.chat.completions.create(
                model="deepseek-chat",
                messages=messages,
                stream=False
            )
 
            final_text.append(response.choices[0].message.content)

        return "\n".join(final_text)

    async def chat_loop(self):
        """运行交互式聊天循环"""
        print("\nMCP 客户端已启动！")
        print("输入你的查询或 'quit' 退出。")

        while True:
            try:
                query = input("\n查询: ").strip()

                if query.lower() == 'quit':
                    break

                response = await self.process_query(query)
                print("\n" + response)

            except Exception as e:
                print(f"\n错误: {str(e)}")

    async def cleanup(self):
        """清理资源"""
        await self.exit_stack.aclose()
        
        if self._session_context:
            await self._session_context.__aexit__(None, None, None)
        if self._streams_context:
            await self._streams_context.__aexit__(None, None, None)


async def main():
    sse = True
    if len(sys.argv) == 2:
        sse = False
        
    client = MCPClient()
    try:
        if sse:
            await client.connect_to_sse()
        else:
            await client.connect_to_server(sys.argv[1])
        await client.chat_loop()
    finally:
        await client.cleanup()

if __name__ == "__main__":
    import sys
    asyncio.run(main())