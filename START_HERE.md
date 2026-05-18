# 从这里开始：30 天学会 Python + 理解全栈

> 面向有 JavaScript/TypeScript 经验的前端开发者。按本文顺序学习，可以**从零掌握 Python**，并在最后**亲手跑通前后端联调**。

## 你将学到什么

| 阶段 | 时间 | 产出 |
|------|------|------|
| 基础语法 | 第 1 周 | 能独立写脚本、读懂 Python 代码 |
| 核心能力 | 第 2 周 | 数据结构、函数、OOP、模块 |
| 进阶 + 小项目 | 第 3 周 | CLI Todo、异步、测试、类型 |
| **全栈串联** | 第 4 周 | FastAPI 后端 + React 前端 CRUD |

---

## 推荐学习顺序（务必按编号）

### 第 1 周：Python 语言基础

| 天 | 做什么 | 文件 |
|----|--------|------|
| 1 | 环境 + Hello World | `01_basics/01_hello_world.py` |
| 2 | 变量与类型 | `01_basics/02_variables.py` |
| 3 | 运算符 | `01_basics/03_operators.py` |
| 4 | 流程控制 | `01_basics/04_control_flow.py` |
| 5 | 复习 + 练习 | `EXERCISES.md` → 01_basics |
| 6 | 列表 | `02_data_structures/01_lists.py` |
| 7 | 字典（最重要） | `02_data_structures/04_dictionaries.py` |

**每天动作**：运行示例 → 改几行观察输出 → 做对应练习。

**卡住时**：打开 `06_frontend_comparison/01_comparison.md` 查 JS 对照。

### 第 2 周：函数与面向对象

| 天 | 文件 |
|----|------|
| 8 | `02_data_structures/02_tuples.py`, `03_sets.py` |
| 9-10 | `03_functions/` 全部 |
| 11-12 | `04_oop/` 全部 |
| 13 | `05_modules_packages/` |
| 14 | 周复习：`EXERCISES.md` 02–05 章 |

### 第 3 周：文件、进阶、综合项目

| 天 | 文件 |
|----|------|
| 15-16 | `07_file_handling/` |
| 17 | `08_advanced/01_decorators.py` |
| 18 | `08_advanced/02_generators.py`, `03_context_managers.py` |
| 19 | **`09_practical_example.py`**（CLI Todo，重要里程碑） |
| 20-21 | `10_async_programming/` |
| 22-23 | `11_testing/`, `12_type_hints/` |

**里程碑**：跑通 `python 09_practical_example.py`，能增删改查本地 `todos.json`。

### 第 4 周：理解前后端 + 全栈实战

| 天 | 做什么 |
|----|--------|
| 24 | 阅读 **`FULLSTACK_GUIDE.md`**（前后端如何通信） |
| 25 | `13_fullstack_bridge/` 示例 + 练习 |
| 26-27 | `python-project-demo`：启动 API，用 Swagger 测 CRUD |
| 28-29 | `react-frontend-demo`：前端调用同一套 API |
| 30 | 对照 `python-project-demo/docs/project-call-flow.md` 走读一遍请求链路 |

**最终验收**（全部通过即算学会）：

```bash
# 终端 1：后端
cd python-project-demo && source venv/bin/activate && pip install -r requirements.txt && python manage.py dev

# 终端 2：前端
cd react-frontend-demo && npm install && npm run dev
```

浏览器打开 http://localhost:5173 ，能创建/编辑/删除 Item；打开 http://localhost:8000/docs 能看到同一数据的 API。

---

## 三个项目的关系（一张图）

```
09_practical_example.py          python-project-demo           react-frontend-demo
     (CLI Todo)          →            (REST API)          →         (React UI)
  命令行 + todos.json              FastAPI + SQLite              axios + 页面
  你输入命令                        浏览器/前端发 HTTP              用户点按钮
  Python 读写文件                   Python 读写数据库              TS 发请求展示 JSON
```

**核心领悟**：前端不会直接碰数据库；后端把数据变成 JSON；前端用 HTTP 请求拿到 JSON 再渲染。CLI Todo 里的「读写在本地文件」在后端项目里变成了「读写在数据库 + 通过 URL 暴露」。

详见 [FULLSTACK_GUIDE.md](./FULLSTACK_GUIDE.md)。

---

## 每天 30 分钟也能学

- **15 分钟**：读 + 运行一个 `.py` 文件
- **10 分钟**：做 `EXERCISES.md` 里 1 道题
---

## 文档索引

| 文档 | 用途 |
|------|------|
| [README.md](./README.md) | 项目总览 |
| **本文 START_HERE.md** | 学习路线（首选入口） |
| [FULLSTACK_GUIDE.md](./FULLSTACK_GUIDE.md) | 前后端如何协作 |
| [EXERCISES.md](./EXERCISES.md) | 练习题 |
| [06_frontend_comparison/01_comparison.md](./06_frontend_comparison/01_comparison.md) | JS ↔ Python 速查 |

---

**下一步**：若环境已就绪，运行 `python 01_basics/01_hello_world.py`；若已学完 Todo，打开 [FULLSTACK_GUIDE.md](./FULLSTACK_GUIDE.md)。
