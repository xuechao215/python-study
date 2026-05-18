# 13_fullstack_bridge/01_http_client.py
# 用 Python 扮演「前端」：向 FastAPI 发 HTTP 请求
# 先启动后端: cd python-project-demo && python manage.py dev

"""
对照前端 axios 代码（react-frontend-demo/src/lib/api.ts）:

  axios.get('/api/v1/items/')     →  client.get(...)
  axios.post('/api/v1/items/', {}) → client.post(...)
"""

import json
import sys

try:
    import httpx
except ImportError:
    print("请先安装: pip install httpx")
    print("或在 python-project-demo 的 venv 中运行本脚本")
    sys.exit(1)

BASE_URL = "http://localhost:8000/api/v1"


def pretty(data):
    print(json.dumps(data, indent=2, ensure_ascii=False))


def main():
    print("=== 1. GET 获取列表（对应 React itemApi.getAll）===\n")
    with httpx.Client(base_url=BASE_URL, timeout=10.0) as client:
        try:
            r = client.get("/items/")
            r.raise_for_status()
        except httpx.ConnectError:
            print("无法连接后端。请先运行: cd python-project-demo && python manage.py dev")
            sys.exit(1)

        items = r.json()
        pretty(items)

        print("\n=== 2. POST 创建一条（对应 itemApi.create）===\n")
        new_item = {
            "title": "Python 客户端创建",
            "description": "由 01_http_client.py 写入",
            "price": 9.9,
            "tax": 0.5,
        }
        r = client.post("/items/", json=new_item)
        r.raise_for_status()
        created = r.json()
        pretty(created)
        item_id = created["id"]

        print(f"\n=== 3. GET 单条 id={item_id} ===\n")
        r = client.get(f"/items/{item_id}")
        pretty(r.json())

        print("\n=== 4. PUT 更新 ===\n")
        r = client.put(
            f"/items/{item_id}",
            json={"title": "已更新标题", "is_active": True},
        )
        pretty(r.json())

        print("\n=== 5. DELETE 删除 ===\n")
        r = client.delete(f"/items/{item_id}")
        pretty(r.json())

        print("\n完成。请在浏览器打开 http://localhost:8000/docs 对比 Try it out 的请求。")


if __name__ == "__main__":
    main()
