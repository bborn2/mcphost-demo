[![MseeP.ai Security Assessment Badge](https://mseep.net/pr/bborn2-mcphost-demo-badge.png)](https://mseep.ai/app/bborn2-mcphost-demo)

## MCP Demo
mcp host demo, include mcp client and mcp server(sse and stdio). 

**Access LLM using OpenAI-compatible protocol**

### install
```
echo "DEEPSEEK_API_KEY=xxx" >> .env
echo "\nAMAP_KEY=xxx" >> .env
uv venv
source .venv/bin/activate
```

### run 
stdio
```
uv run client.py mcpserver-weather.py
```

sse
```
uv run client.py
```

### example
query:
```
ca forecast
--------------
[调用工具 get_forecast，参数 {'latitude': 36.7783, 'longitude': -119.4179}]
Here’s the current weather forecast for California (based on coordinates near the state's center):

### **Today**  
☀️ **Sunny**  
- **High:** 62°F  
- **Wind:** 0-5 mph (WSW)  

### **Tonight**  
🌤️ **Mostly Clear**  
- **Low:** 42°F  
- **Wind:** 5 mph (NE)  

### **Friday**  
☀️ **Sunny**  
- **High:** 68°F  
- **Wind:** 5 mph (SSE)  

### **Friday Night**  
🌙 **Clear**  
- **Low:** 45°F  
- **Wind:** 5 mph (NNE)  

### **Saturday**  
☀️ **Sunny & Warmer**  
- **High:** 73°F  
- **Wind:** 5 mph (W)  

*Note: This is a general forecast; conditions may vary by region (e.g., coastal, inland, mountainous). Let me know if you'd like details for a specific city!*
```


query:
```
北京到武汉有多远
--------------
[调用工具 maps_geo，参数 {'address': '北京'}]
北京到武汉的直线距离约为**1,150公里**，实际交通距离会因路线不同有所差异：

1. **高铁**：最快约4-5小时（京广高铁，约1,200公里）
2. **驾车**：约12小时（京港澳高速，约1,200公里）
3. **飞行**：直飞约1.5小时（空中距离约1,050公里）

建议使用导航软件（如百度地图/高德地图）获取实时路线规划。需要更具体的出行信息可随时告知！

```
