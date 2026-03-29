# Python Demo Project - FastAPI

这是一个为前端开发者准备的 Python 示例项目，演示了现代 Python 开发的工程化实践。
它使用 [FastAPI](https://fastapi.tiangolo.com/) 构建了一个简单的 REST API。

## 功能

- RESTful API (GET, POST, PUT, DELETE)
- 自动生成 Swagger 文档 (`/docs`)
- 类型检查 (Type Hints)
- 数据验证 (Pydantic)

## 快速开始 (使用 venv)

如果你习惯使用 npm/yarn，这里是对应的 Python 工作流。

### 1. 环境准备

**Python 中的 `venv` 类似于 `node_modules`，但它不放在项目目录下，而是作为一个独立的环境。**

```bash
# 1. 创建虚拟环境 (只需执行一次)
# Windows
python -m venv venv
# macOS/Linux
python3 -m venv venv

# 2. 激活虚拟环境 (每次开发前都需要执行)
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# 激活成功后，你的命令行提示符前会出现 (venv) 字样
```

### 2. 安装依赖

类似于 `npm install`。

```bash
pip install -r requirements.txt
```

### 3. 运行项目

类似于 `npm run dev`。

```bash
# 在项目根目录下运行
python -m app.main
# 或者直接使用 uvicorn
uvicorn app.main:app --reload
```

启动后访问:
- **API 文档 (Swagger UI)**: http://localhost:8000/docs
- **API 文档 (ReDoc)**: http://localhost:8000/redoc
- **API 根路径**: http://localhost:8000/api/items

---

## 进阶：使用 Poetry (推荐)

[Poetry](https://python-poetry.org/) 是现代 Python 的包管理工具，类似于 JS 中的 `yarn` 或 `pnpm`。它解决了 `pip` + `requirements.txt` 的很多痛点（如依赖冲突、没有锁文件等）。

### 对比表

| 功能 | npm / yarn | pip + venv | Poetry |
| :--- | :--- | :--- | :--- |
| **初始化项目** | `npm init` | 手动创建 | `poetry init` |
| **安装依赖** | `npm install <pkg>` | `pip install <pkg>` | `poetry add <pkg>` |
| **开发依赖** | `npm i -D <pkg>` | 无内置支持 | `poetry add -D <pkg>` |
| **锁文件** | `package-lock.json` | 无 | `poetry.lock` |
| **运行脚本** | `npm run <script>` | 无 | `poetry run <cmd>` |
| **虚拟环境** | `node_modules` (自动) | 手动创建/激活 | 自动管理 |

### 使用 Poetry 运行本项目

1.  **安装 Poetry**:
    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```

2.  **初始化/安装依赖**:
    ```bash
    # 如果已有 pyproject.toml
    poetry install
    ```

3.  **运行项目**:
    ```bash
    poetry run uvicorn app.main:app --reload
    ```

## 项目结构

```
python-project-demo/
├── app/
│   ├── __init__.py
│   ├── main.py          # 入口文件 (App entry point)
│   ├── core/            # 核心逻辑 (Database, Config)
│   ├── models/          # 数据模型 (Pydantic Schemas)
│   └── routers/         # 路由定义 (API Routes)
├── tests/               # 测试文件
├── requirements.txt     # 依赖列表 (pip)
└── README.md            # 项目文档
```

## API 接口

- `GET /api/items`: 获取所有项目
- `POST /api/items`: 创建新项目
- `GET /api/items/{id}`: 获取详情
- `PUT /api/items/{id}`: 更新项目
- `DELETE /api/items/{id}`: 删除项目
