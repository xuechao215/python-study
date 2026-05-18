# 第 13 章：全栈衔接（前端 ↔ Python 后端）

学完 `09_practical_example.py` 后、进入 `python-project-demo` 之前，请完成本章。

## 学习目标

- 理解 HTTP 方法（GET/POST/PUT/DELETE）与 CRUD 的对应
- 会用 Python 脚本调用自己的 FastAPI（相当于前端的 `fetch` / `axios`）
- 建立「URL + JSON + 状态码」的心智模型

## 文件说明

| 文件 | 内容 |
|------|------|
| `01_http_client.py` | 用 httpx 调用本地 API（需先启动后端） |
| `02_request_flow.md` | 与 React 并排对照的请求链路 |

## 前置条件

```bash
cd python-project-demo
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py dev
```

另开终端运行本章脚本。

## 下一步

阅读 [FULLSTACK_GUIDE.md](../FULLSTACK_GUIDE.md)，然后启动 `react-frontend-demo`。
