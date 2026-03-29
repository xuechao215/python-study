# React Frontend Demo

这是一个基于 Vite + React + TypeScript + Tailwind CSS 的前端项目，用于演示如何与 Python (FastAPI) 后端进行交互。

## 功能

- **展示项目列表**: 对应 GET `/items`
- **创建新项目**: 对应 POST `/items`
- **编辑项目**: 对应 PUT `/items/{id}`
- **删除项目**: 对应 DELETE `/items/{id}`

## 快速开始

### 1. 启动后端

确保 `python-project-demo` 已经在运行：

```bash
cd python-project-demo
# 激活虚拟环境
source venv/bin/activate
# 启动服务
python manage.py dev
```

后端服务应该运行在 `http://localhost:8000`。

### 2. 启动前端

在当前目录 (`react-frontend-demo`) 下：

```bash
# 安装依赖 (如果你还没安装)
npm install

# 启动开发服务器
npm run dev
```

前端服务通常运行在 `http://localhost:5173`。

## 关键代码说明

1.  **`src/lib/api.ts`**: 使用 `axios` 封装了 API 请求，配置了 baseURL 为 Python 后端地址。
2.  **`src/types/index.ts`**: 定义了 TypeScript 接口，与后端的 Pydantic 模型对应。
3.  **`src/components/ItemList.tsx`**: 主要的 CRUD 逻辑和 UI 展示。
4.  **`src/components/ItemForm.tsx`**: 复用的表单组件，用于创建和编辑。

## 常见问题

- **CORS 错误**: 如果控制台报错 "Access to XMLHttpRequest ... has been blocked by CORS policy"，请检查后端 `app/main.py` 中是否配置了 `CORSMiddleware` 并且允许了 `http://localhost:5173`。
- **连接失败**: 确保后端服务正在运行，且端口号正确 (8000)。
