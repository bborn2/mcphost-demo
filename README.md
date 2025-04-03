## MCP Demo
mcp host demo, include mcp client and mcp server. 

**Access LLM using OpenAI-compatible protocol**

### install
```
echo "DEEPSEEK_API_KEY=xxx" >> .env
uv venv
source .venv/bin/activate
```

### run 
```
uv run client.py mcpserver-weather.py
```

### example
```
query: ca forecast
```
``` 

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
