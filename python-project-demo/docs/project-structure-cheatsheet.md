# python-project-demo 项目结构速查表

这份文档适合你在阅读项目时快速翻看。

如果前两份文档是“详细讲解版”，这份就是“查字典版”。

- 详细版 1：[project-call-flow.md](./project-call-flow.md)
- 详细版 2：[request-lifecycle.md](./request-lifecycle.md)

---

## 1. 项目目录速查

```text
python-project-demo/
├── app/                  # 主业务代码
├── tests/                # 测试代码
├── docs/                 # 学习文档
├── manage.py             # 命令入口
├── requirements.txt      # 依赖列表
├── Dockerfile            # Docker 镜像构建文件
├── docker-compose.yml    # Docker 启动编排文件
└── README.md             # 项目说明
```

---

## 2. app 目录速查

```text
app/
├── api/                  # 路由层，处理 HTTP 请求
├── core/                 # 核心配置
├── crud/                 # 数据库操作层
├── db/                   # 数据库基础设施
├── models/               # ORM 模型
├── schemas/              # 请求/响应数据结构
└── main.py               # 应用启动入口
```

---

## 3. 一句话理解每个目录

| 目录/文件 | 作用 | 可以类比成什么 |
| :--- | :--- | :--- |
| `manage.py` | 运行项目常用命令 | `package.json` scripts |
| `app/main.py` | 应用入口，组装整个项目 | `server.js` / `main.tsx` |
| `app/api/` | 定义接口和路由 | Express Router / Controller |
| `app/schemas/` | 校验请求和约束响应 | TS 类型 + 表单校验 |
| `app/models/` | 定义数据库表结构 | ORM Entity |
| `app/crud/` | 封装增删改查 | service / DAO |
| `app/db/` | 提供数据库连接和 Session | 数据库连接层 |
| `app/core/` | 全局配置 | config/env |
| `tests/` | 自动化测试 | 单元测试 / 接口测试 |
| `docs/` | 学习笔记和结构说明 | 项目文档 |

---

## 4. 看到一个请求时，先找哪几个地方

假设你看到一个接口：

```text
POST /api/v1/items/
```

建议按这个顺序找代码：

1. `app/main.py`：总入口，确认总前缀怎么注册
2. `app/api/v1/api.py`：确认这个模块挂在哪个前缀下
3. `app/api/v1/endpoints/items.py`：找到具体接口函数
4. `app/schemas/item.py`：看请求体和响应体结构
5. `app/crud/item.py`：看具体数据库操作
6. `app/models/item.py`：看对应表结构
7. `app/db/session.py`：看数据库会话怎么来的

---

## 5. 初学者最容易混淆的概念

### 5.1 `models` 和 `schemas` 的区别

#### `models`
面向数据库。

作用：定义表长什么样。

#### `schemas`
面向接口。

作用：定义请求和响应长什么样。

一句话记忆：

> `models` 管数据库，`schemas` 管接口。

---

### 5.2 `crud` 和 `api` 的区别

#### `api`
负责接请求、收参数、返回响应。

#### `crud`
负责查库、写库、更新、删除。

一句话记忆：

> `api` 负责接待，`crud` 负责干活。

---

### 5.3 `main.py` 和 `manage.py` 的区别

#### `main.py`
真正的应用入口。

#### `manage.py`
方便你执行命令的脚本入口。

一句话记忆：

> `manage.py` 是命令助手，`main.py` 是应用入口。

---

## 6. 这个项目的主流程速记

```text
请求进入 main.py
→ 分发到 api
→ schema 校验数据
→ get_db 提供数据库会话
→ crud 操作 model
→ 写入数据库
→ 返回响应
```

一句话版本：

> main 组装项目，api 接请求，schema 校验，crud 查库，model 定义表。

---

## 7. 你现在最值得优先理解的文件

如果你是初学者，建议优先看这几个：

1. `app/main.py`
2. `app/api/v1/endpoints/items.py`
3. `app/schemas/item.py`
4. `app/crud/item.py`
5. `app/models/item.py`
6. `app/db/session.py`

如果这 6 个文件看懂了，这个项目的大骨架你基本就懂了。

---

## 8. 推荐阅读顺序

### 第一遍：只看整体
- `README.md`
- `docs/project-call-flow.md`
- `docs/project-structure-cheatsheet.md`

### 第二遍：只跟一条请求
- `docs/request-lifecycle.md`
- `app/api/v1/endpoints/items.py`
- `app/crud/item.py`

### 第三遍：补数据库和配置
- `app/models/item.py`
- `app/db/session.py`
- `app/core/config.py`

---

## 9. 文档导航

- [项目调用关系图解](./project-call-flow.md)
- [请求执行顺序讲解](./request-lifecycle.md)
- [README](../README.md)
