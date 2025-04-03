## MCP Demo
mcp host demo, include mcp client and mcp server. 

**Access LLM using OpenAI-compatible protocol**

### install
```
uv venv
source .venv/bin/activate
uv pip sync pyproject.toml
```

### run server
```
uv run weather.py
```

### run client
```
python client.py ./weather/weather.py
```

### env
add .env file
```
DEEPSEEK_API_KEY=xxx
```
