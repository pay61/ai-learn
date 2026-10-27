import requests
import json
'''
    写 fetch_day03.py：

对公开接口发 GET
完整 JSON 写入同目录 response.json
再打印若干字段
首选：https://httpbin.org/json
备选：https://jsonplaceholder.typicode.com/users
'''
url = "https://httpbin.org/json"
# 若上面连不上，改成下一行：
# url = "https://jsonplaceholder.typicode.com/users"
resp = requests.get(url, timeout=15)
resp.raise_for_status()
data = resp.json()
with open("response.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("已保存 response.json")
if isinstance(data, dict) and "slideshow" in data:
    show = data["slideshow"]
    print("title:", show.get("title"))
    print("author:", show.get("author"))
elif isinstance(data, list):
    for user in data[:3]:
        print(user.get("name"), user.get("email"))
else:
    print(data)
