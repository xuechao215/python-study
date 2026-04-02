# python-project-demo 项目调用关系图解

这份文档的目标是帮助初学者先建立整体感：**这个项目有哪些层，它们之间是怎么配合的。**

如果你把这个项目看成一家餐厅，那么：
- `main.py` 是总入口
- `api/` 是前台接待
- `schemas/` 是点单规则
- `crud/` 是真正干活的人
- `models/` 是数据库表定义
- `db/` 是数据库连接基础设施
- `core/` 是配置中心

---

## 1. 整体调用关系图

```text
浏览器 / 前端 / Swagger
          │
          ▼
   HTTP 请求（GET/POST/PUT/DELETE）
          │
          ▼
app/main.py
  FastAPI 应用入口
  - 创建 app
  - 注册路由
  - 配置 CORS
          │
          ▼
app/api/v1/api.py
  总路由分发器
          │
          ▼
app/api/v1/endpoints/items.py
  具体接口处理层
  - 接收请求
  - 参数声明
  - 调用 CRUD
  - 返回响应
          │
          ├──────────────► app/schemas/item.py
          │                 Pydantic 校验/响应模型
          │                 - 校验请求体
          │                 - 规范返回结构
          │
          └──────────────► app/db/session.py
                            提供数据库会话 get_db()
                            │
                            ▼
                     app/crud/item.py
                       数据库操作层
                       - 查询
                       - 新增
                       - 更新
                       - 删除
                            │
                            ▼
                     app/models/item.py
                       ORM 模型
                       - 对应数据库表 items
                            │
                            ▼
                        SQLite 数据库
```

---

## 2. 各层职责说明

### 2.1 `manage.py`

作用：项目命令入口。

它类似前端项目中的脚本命令包装器，你可以通过它执行：

```bash
python manage.py install
python manage.py dev
python manage.py test
```

它本身不是 Web 应用核心逻辑，而是帮助你更方便地运行项目。

---

### 2.2 `app/main.py`

作用：应用总入口。

它主要做这些事：

1. 创建 FastAPI 应用
2. 注册总路由
3. 配置跨域 CORS
4. 初始化数据库表
5. 提供根路径 `/`

可以把它理解为：**把整个项目组装起来的地方。**

---

### 2.3 `app/api/v1/api.py`

作用：总路由汇总。

这个文件不处理具体业务，它只是把不同模块的路由统一注册起来。

比如当前项目里：
- 把 `items` 路由挂到 `/items`

再结合 `main.py` 中的 `/api/v1` 前缀，最终形成：

```text
/api/v1/items
```

---

### 2.4 `app/api/v1/endpoints/items.py`

作用：具体接口处理层。

这里定义了项目的增删改查接口：
- `GET /api/v1/items/`
- `POST /api/v1/items/`
- `GET /api/v1/items/{item_id}`
- `PUT /api/v1/items/{item_id}`
- `DELETE /api/v1/items/{item_id}`

这一层负责：
- 接收 HTTP 请求
- 声明参数
- 调用数据库操作逻辑
- 处理不存在等异常
- 返回响应

你可以把它类比成：
- Express Router
- NestJS Controller

---

### 2.5 `app/schemas/item.py`

作用：数据校验和响应结构定义。

这里使用的是 Pydantic 模型，负责：
- 校验客户端传来的 JSON 是否符合要求
- 限制返回给前端的数据结构
- 自动生成接口文档

当前项目中的几个模型：

- `ItemBase`：公共字段
- `ItemCreate`：创建时用
- `ItemUpdate`：更新时用
- `Item`：响应时用

这层非常重要，因为它把“接口数据格式”单独抽离出来了。

---

### 2.6 `app/crud/item.py`

作用：数据库操作层。

CRUD 是：
- Create
- Read
- Update
- Delete

这一层封装了：
- `get_item()`
- `get_items()`
- `create_item()`
- `update_item()`
- `delete_item()`

它的核心思想是：
**路由层不直接写数据库细节，而是交给 CRUD 层处理。**

这样代码更清晰，也更容易复用。

---

### 2.7 `app/models/item.py`

作用：数据库表结构定义。

这里的 `Item` 是 SQLAlchemy ORM 模型，对应数据库中的 `items` 表。

它定义了表里的字段：
- `id`
- `title`
- `description`
- `price`
- `tax`
- `is_active`

这层面向的是数据库，不是 API 输入输出。

---

### 2.8 `app/db/session.py`

作用：数据库连接与会话管理。

这里有两个关键概念：

#### Engine
表示和数据库建立连接的能力。

#### Session
表示一次数据库操作会话。

还提供了一个很重要的函数：

```python
def get_db():
    ...
```

它用于 FastAPI 的依赖注入。每个请求需要访问数据库时，都可以通过它获得一个 `db` 会话，用完后自动关闭。

---

### 2.9 `app/db/base.py`

作用：ORM 基类。

所有数据库模型都继承这个 `Base`，这样 SQLAlchemy 才能知道哪些类属于 ORM 模型，并基于它们创建表。

---

### 2.10 `app/core/config.py`

作用：项目配置中心。

这里定义了：
- 项目名
- API 前缀
- 数据库地址

它支持从 `.env` 文件读取配置。

这体现的是工程化中的一个重要原则：
**配置和业务代码分离。**

---

### 2.11 `tests/test_main.py`

作用：接口测试。

这个测试文件做了这些事：
- 创建内存数据库
- 替换正式数据库依赖
- 用测试客户端发请求
- 验证接口结果

初学者可以把它理解为：
**用代码自动检查接口是否真的能工作。**

---

## 3. 这个项目最重要的三条线

### 3.1 启动线

```text
manage.py → app/main.py
```

意思：你执行启动命令后，最终是由 `main.py` 把 FastAPI 应用跑起来。

---

### 3.2 请求线

```text
main.py → api.py → endpoints/items.py
```

意思：请求先进入应用，再被分发到具体路由函数。

---

### 3.3 数据线

```text
endpoints/items.py → schemas/item.py → crud/item.py → models/item.py → 数据库
```

意思：请求数据先被校验，再执行数据库操作，最后返回结果。

---

## 4. 为什么要这样分层

如果所有代码都写进一个文件，项目会很快变得难以维护。

分层后的好处：

1. **职责清晰**：每层只做自己该做的事
2. **更容易定位问题**：改接口就去 `api`，改表结构就去 `models`
3. **更容易测试**：不同层可以拆开验证
4. **更接近真实项目**：这是后端项目里很常见的组织方式

---

## 5. 初学者建议怎么理解这张图

建议你先记住这一句话：

> `main.py` 负责启动应用，`api` 负责接请求，`schemas` 负责校验数据，`crud` 负责操作数据库，`models` 负责定义表结构，`db` 负责提供数据库连接。

如果这句话你能看懂七八成，就说明你已经抓住这个项目的主骨架了。
