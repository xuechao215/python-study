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

## 学习文档导航

如果你想按“先整体、再细节”的顺序学习这个项目，可以先看下面几份文档：

- [项目调用关系图解](docs/project-call-flow.md)：先理解这个项目有哪些层，它们如何配合
- [请求执行顺序讲解](docs/request-lifecycle.md)：再理解一个请求是怎么一步一步执行的
- [项目结构速查表](docs/project-structure-cheatsheet.md)：适合随时回来看概念和目录作用

---

## 项目结构详解

这个项目是一个典型的 **FastAPI + SQLAlchemy + Pydantic** 的后端项目，适合初学者理解“一个 Python Web 项目通常由哪些部分组成”。

### 一、先看整体目录

```text
python-project-demo/
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── api.py
│   │       └── endpoints/
│   │           └── items.py
│   ├── core/
│   │   └── config.py
│   ├── crud/
│   │   └── item.py
│   ├── db/
│   │   ├── base.py
│   │   └── session.py
│   ├── models/
│   │   └── item.py
│   ├── schemas/
│   │   └── item.py
│   └── main.py
├── tests/
│   └── test_main.py
├── manage.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

### 二、每一层是干什么的

#### 1. `manage.py`：项目脚本入口
文件位置：[manage.py](manage.py)

它类似前端项目里的脚本命令入口，作用像 `package.json` 里的 scripts。

你可以执行：

```bash
python manage.py install
python manage.py dev
python manage.py test
```

它内部通过 `subprocess` 去执行真正的命令，比如启动 `uvicorn` 或安装依赖。对于初学者来说，可以把它理解为“把常用命令包装起来，方便记忆和执行”。

---

#### 2. `app/main.py`：应用启动入口
文件位置：[app/main.py](app/main.py)

这是整个 FastAPI 应用的入口，作用相当于：
- 前端里的 `main.tsx` / `index.js`
- Node.js 项目里的 `server.js`

它做了几件核心事情：

1. 创建数据库表
2. 创建 FastAPI 应用对象
3. 配置 CORS
4. 注册路由
5. 提供根路径 `/`

也就是说，**main.py 负责把项目的各个模块组装起来**。

---

#### 3. `app/api/`：路由层
文件位置：[app/api/v1/api.py](app/api/v1/api.py)、[app/api/v1/endpoints/items.py](app/api/v1/endpoints/items.py)

这一层负责处理 HTTP 请求，类似前端请求到后端时最先进入的控制器层，也类似：
- Express 里的 router
- NestJS 里的 controller

其中：

- `api.py`：统一注册各个业务路由
- `endpoints/items.py`：定义 items 相关接口

在 `items.py` 里你能看到：
- `@router.get("/")`
- `@router.post("/")`
- `@router.put("/{item_id}")`
- `@router.delete("/{item_id}")`

这些装饰器就是在声明 API 路径和请求方法。

这一层主要负责：
- 接收请求参数
- 调用 CRUD/业务逻辑
- 处理异常
- 返回响应

一般来说，**路由层不要写太多数据库细节**，而是把具体操作交给下层。

---

#### 4. `app/schemas/`：数据校验与响应结构
文件位置：[app/schemas/item.py](app/schemas/item.py)

这里放的是 **Pydantic 模型**，主要用于：
- 校验请求参数
- 约束响应结构
- 生成 Swagger/OpenAPI 文档

这是 Python Web 项目里非常重要的一层。

比如：
- `ItemCreate`：定义创建数据时客户端必须传什么
- `ItemUpdate`：定义更新时允许传什么
- `Item`：定义接口返回的数据长什么样

你可以这样理解：

- `models/` 更像数据库结构
- `schemas/` 更像接口层的数据契约

前端类比：
- 有点像 TypeScript interface/type + 表单校验规则 的结合体

为什么要分开？
因为数据库表结构和接口传输结构，通常不是完全一样的。分层后更清晰，也更安全。

---

#### 5. `app/models/`：数据库模型层
文件位置：[app/models/item.py](app/models/item.py)

这里放的是 **SQLAlchemy ORM 模型**，用于描述数据库表。

例如 `Item` 模型定义了：
- 表名 `items`
- 字段 `id`
- `title`
- `description`
- `price`
- `tax`
- `is_active`

这层可以类比为：
- Django 的 Model
- Java 里的 Entity
- TypeORM 的 Entity
- Prisma schema 对应的实体映射概念

重点要区分：

- `models` 面向数据库
- `schemas` 面向 API 输入输出

初学者最容易混淆的就是这两层。

---

#### 6. `app/crud/`：数据库操作层
文件位置：[app/crud/item.py](app/crud/item.py)

CRUD = Create / Read / Update / Delete。

这一层专门负责对数据库做实际操作，比如：
- `get_item()`
- `get_items()`
- `create_item()`
- `update_item()`
- `delete_item()`

它的作用是把“查数据库、写数据库”的逻辑从路由层拆出去。

这样做的好处：
- 路由更简洁
- 逻辑更容易复用
- 更方便测试
- 分层更清楚

你可以把它理解为：
- Service 层 / DAO 层的简化版本

这个项目里 CRUD 层还不算复杂，但已经很好地体现了后端项目分层思想。

---

#### 7. `app/db/`：数据库基础设施
文件位置：[app/db/session.py](app/db/session.py)、[app/db/base.py](app/db/base.py)

这部分是数据库运行的底层配置。

- `base.py`：定义所有 ORM 模型继承的基类 `Base`
- `session.py`：创建数据库引擎和 Session，并提供 `get_db()`

这里的几个概念非常关键：

##### Engine
可以理解为“数据库连接能力”。

##### Session
可以理解为“当前这次数据库操作的会话对象”。

在 FastAPI 里，一个请求通常会拿到一个独立的 Session，请求结束后关闭。

##### `get_db()`
这是一个依赖注入函数，FastAPI 会自动把数据库会话传给接口函数。

类似：
- Express 中间件提前准备好某个对象，然后挂到 request 上
- 依赖注入容器帮你自动提供资源

---

#### 8. `app/core/`：核心配置
文件位置：[app/core/config.py](app/core/config.py)

这里放的是项目的全局配置，例如：
- 项目名
- API 前缀
- 数据库连接地址

它使用了 `pydantic-settings`，支持从 `.env` 文件读取环境变量。

这是 Python 项目里非常常见的做法。

比如：
- 开发环境用 SQLite
- 生产环境改成 PostgreSQL

你不需要修改业务代码，只需要改配置。

这体现了一个很重要的工程化思想：
**配置和代码分离。**

---

#### 9. `tests/`：测试目录
文件位置：[tests/test_main.py](tests/test_main.py)

这里放自动化测试。

这个测试文件做了几件事：
- 创建内存数据库
- 覆盖正式环境的数据库依赖
- 使用 `TestClient` 模拟 HTTP 请求
- 测试增删改查接口

这是后端项目里很重要的一部分，因为它能验证：
- 接口是否正常
- 参数处理是否正确
- 数据库逻辑是否可用

对于初学者，你可以先记住一句话：
**tests 目录就是用代码来验证代码。**

---

#### 10. `requirements.txt`：依赖清单
文件位置：[requirements.txt](requirements.txt)

它类似前端里的 `package.json` 里 dependencies 的一部分，但更简单，主要记录依赖包。

例如：
- `fastapi`：Web 框架
- `uvicorn`：ASGI 服务器
- `pydantic`：数据校验
- `sqlalchemy`：ORM
- `pytest`：测试框架
- `black`：代码格式化
- `ruff`：Lint 工具

安装方式：

```bash
pip install -r requirements.txt
```

---

#### 11. `Dockerfile` 和 `docker-compose.yml`：容器化部署
文件位置：[Dockerfile](Dockerfile)、[docker-compose.yml](docker-compose.yml)

它们用于把项目放进 Docker 容器里运行。

- `Dockerfile`：定义“镜像怎么构建”
- `docker-compose.yml`：定义“容器怎么启动、映射端口、挂载目录、设置环境变量”

对初学者来说，你可以先把它理解成：
- `Dockerfile` = 项目的运行说明书
- `docker-compose.yml` = 多个运行配置的启动编排文件

如果你现在主要是学习 Python 本身，这部分先知道用途就够了。

---

### 三、这个项目的请求流转过程

当你请求一个接口，例如：

```http
POST /api/v1/items/
```

项目内部大致会这样流转：

1. 请求进入 `app/main.py`
2. 被路由分发到 `app/api/v1/endpoints/items.py`
3. FastAPI 用 `schemas/item.py` 校验请求体
4. 路由函数通过 `Depends(get_db)` 拿到数据库会话
5. 路由调用 `crud/item.py` 进行数据库写入
6. CRUD 层操作 `models/item.py` 对应的表
7. 结果返回给路由
8. FastAPI 再按 `response_model` 转成规范 JSON 响应

这就是一个典型的 Python 后端项目的数据流。

---

### 四、一个 Python 项目通常由哪些部分构成

不只是这个示例，大多数 Python 项目都会包含下面这些组成部分。

#### 1. 入口文件
例如：
- `main.py`
- `app.py`
- `manage.py`
- `run.py`

作用：程序从哪里启动。

---

#### 2. 业务代码目录
例如：
- `app/`
- `src/`
- `project_name/`

作用：存放主要业务逻辑。

---

#### 3. 配置文件
例如：
- `.env`
- `config.py`
- `settings.py`
- `pyproject.toml`
- `requirements.txt`

作用：管理依赖、环境变量、工具配置。

---

#### 4. 数据模型
如果项目涉及数据库，通常会有：
- ORM 模型
- Schema/Serializer
- 数据库连接配置

---

#### 5. 测试目录
例如：
- `tests/`

作用：写自动化测试。

---

#### 6. 环境管理
例如：
- `venv/`
- `.venv/`
- Poetry 虚拟环境

作用：隔离每个项目的 Python 依赖。

注意：`venv` 一般不建议提交到 Git 仓库。

---

#### 7. 文档文件
例如：
- `README.md`

作用：告诉别人这个项目是干什么的、怎么运行。

---

#### 8. 部署文件
例如：
- `Dockerfile`
- `docker-compose.yml`
- CI 配置

作用：方便部署、测试、自动化运行。

---

### 五、作为初学者，你最应该先理解哪几层

建议你按这个顺序理解：

1. `main.py`：应用怎么启动
2. `items.py`：接口怎么定义
3. `schemas/item.py`：请求和响应怎么校验
4. `crud/item.py`：数据库操作怎么封装
5. `models/item.py`：数据库表怎么定义
6. `session.py`：数据库连接怎么提供
7. `config.py`：配置怎么读取

这个顺序是因为它最接近“用户发起请求后，代码如何一步步执行”。

---

### 六、给前端初学者的一个类比

如果你有前端背景，可以这样快速建立映射：

| Python/FastAPI | 前端/Node 常见类比 |
| :--- | :--- |
| `main.py` | `main.tsx` / `server.js` |
| `api/endpoints` | Express Router / Controller |
| `schemas` | TS 类型 + 表单校验 |
| `models` | ORM Entity / 数据表定义 |
| `crud` | service / data access 层 |
| `config.py` | config.ts / env 配置 |
| `requirements.txt` | 依赖清单 |
| `venv` | 隔离依赖环境 |
| `tests/` | 单元测试 / 接口测试 |

---

## API 接口

当前项目提供的主要接口：

- `GET /api/v1/items/`：获取所有项目
- `POST /api/v1/items/`：创建新项目
- `GET /api/v1/items/{id}`：获取单个项目详情
- `PUT /api/v1/items/{id}`：更新项目
- `DELETE /api/v1/items/{id}`：删除项目

你可以启动项目后访问：
- http://localhost:8000/docs

在 Swagger 页面中直接调试这些接口。
