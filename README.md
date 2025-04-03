## MCP Demo
mcp host demo, include mcp client and mcp server. 

**Access LLM using OpenAI-compatible protocol**

### install
```
echo "DEEPSEEK_API_KEY=xxx" >> .env
uv venv
source .venv/bin/activate
```

### run server
```
uv run weather.py
```

### run client
```
uv run client.py ./weather/weather.py
```

### example

```
[调用工具 get_alerts，参数 {'state': 'TX'}]
Here are the current weather alerts for Texas:

### **Flood Alerts** ⚠️🌧️
1. **Flood Watch** (Severe)  
   - **Areas**: Fannin, Lamar, Hunt, Delta, Hopkins, Rains  
   - **Details**: 3-5 inches of rain (isolated up to 8 inches). Flooding possible in low-lying areas.  
   - **Time**: Late tonight through Sunday morning.  

2. **Flood Warnings** (Severe)  
   - **Attoyac Bayou near Chireno** (Nacogdoches, Rusk, San Augustine, Shelby) – Minor flooding until Sunday.  
   - **Angelina River near Lufkin** (Angelina, Cherokee, Nacogdoches) – Minor flooding ongoing.  
   - **Cowleech Fork Sabine River at Greenville** (Hunt) – Minor flooding expected, cresting tonight.  
   - **Sabine River near Deweyville** (Newton, Orange, Beauregard, Calcasieu) – Minor flooding ongoing.  
   - **Sulphur River near Talco** (Franklin, Morris, Red River, Titus) – Flooding expected Saturday.  

3. **Flood Advisory** (Minor)  
   - **Jack County** – Urban/small stream flooding due to heavy rain until 10:45 AM CDT.  

---

### **Wind Advisories** 💨  
- **Coastal & Inland Cameron/Willacy**: Gusts up to **50 mph** (until 5 PM CDT).  
- **Southeast Texas (Harris, Galveston, etc.)**: Gusts up to **30-35 mph**.  
- **Impact**: Unsecured objects may blow around, difficult driving for high-profile vehicles.  

---

### **Coastal & Beach Hazards** 🌊  
- **Coastal Flood Advisory**: Minor flooding in Cameron, Jefferson, and Orange Counties.  
- **High Surf & Rip Currents**: Dangerous waves (5-7 ft) along Gulf-facing beaches.  
- **Beach Hazards**: High risk of rip currents (Galveston, Bolivar Peninsula).  

---

### **Key Recommendations**  
- **Avoid flooded roads** – "Turn around, don’t drown."  
- **Secure outdoor items** due to strong winds.  
- **Stay out of Gulf waters** due to rip currents.  

For real-time updates, check the [National Weather Service](https://www.weather.gov). Stay safe!
```
