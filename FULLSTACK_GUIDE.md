# 全栈指南：前端开发者如何理解 Python 后端

本文把你在浏览器里熟悉的概念，映射到本仓库的三个层次：**CLI Todo → FastAPI → React**。

---

## 1. 你已经会的东西（前端）

在 React 里你经常写：

```typescript
const res = await fetch('/api/items');
const items = await res.json();
setItems(items);
```

等价于：

1. 浏览器向某个 **URL** 发 **HTTP 请求**
2. 服务器返回 **JSON 字符串**
3. 前端 `JSON.parse`（或 `res.json()`）变成对象
4. 用 state 驱动 UI 更新

Python 后端做的事就是：**接收请求 → 查库/算逻辑 → 返回 JSON**。

---

## 2. 本仓库的三层对照

| 概念 | CLI Todo (`09_practical_example.py`) | FastAPI (`python-project-demo`) | React (`react-frontend-demo`) |
|------|--------------------------------------|----------------------------------|-------------------------------|
| 用户操作 | 终端输入 `add 买菜` | HTTP `POST /api/v1/items/` | 点击「New Item」提交表单 |
| 数据载体 | `todos.json` 文件 | SQLite `sql_app.db` | 内存 state（来自 API） |
| 数据结构 | `dict` / `TodoItem` 类 | Pydantic `Item` / SQLAlchemy `Item` 模型 | TypeScript `interface Item` |
| 读列表 | 读文件 + `json.load` | `GET /items` → 查数据库 | `itemApi.getAll()` |
| 增删改 | 写回 `todos.json` | `POST/PUT/DELETE` | `itemApi.create/update/delete` |

**同一业务，三种界面**：命令行、HTTP API、网页。

---

## 3. 一次「创建 Item」的完整链路

```text
[浏览器] 用户填写 title、price，点保存
    │
    ▼
[React] ItemForm.onSubmit → itemApi.create({ title, price, ... })
    │
    ▼  axios.post('http://localhost:8000/api/v1/items/', body)
    │
[网络] HTTP POST + JSON Body + Content-Type: application/json
    │
    ▼
[FastAPI] app/main.py → 路由 /api/v1/items/ → endpoints/items.py
    │
    ▼  Pydantic 校验 body 是否符合 ItemCreate
    │
[CRUD] crud/item.py → create_item() 写入数据库
    │
    ▼
[数据库] SQLite 表 items 多一行
    │
    ▼  返回 ORM 对象 → 转成 Pydantic Item → JSON
    │
[React] 收到 201 + JSON → fetchItems() 重新 GET 列表 → 界面刷新
```

**和 Express 的类比**（若你熟悉 Node）：

| Express | 本仓库 FastAPI |
|---------|----------------|
| `app.use(cors())` | `main.py` 里 `CORSMiddleware` |
| `router.get('/items')` | `endpoints/items.py` 的 `@router.get` |
| `req.body` 校验（如 zod） | Pydantic `ItemCreate` |
| `prisma.item.create` | `crud/item.py` + SQLAlchemy |
| `res.json(item)` | `return item`（FastAPI 自动序列化） |

---

## 4. 类型在三端的对应关系

后端 `app/schemas/item.py`：

```python
class ItemCreate(BaseModel):
    title: str
    price: float
    description: Optional[str] = None
```

前端 `react-frontend-demo/src/types/index.ts`：

```typescript
export interface ItemCreate {
  title: string;
  price: number;
  description?: string;
}
```

| Python | TypeScript | 说明 |
|--------|------------|------|
| `str` | `string` | |
| `int` | `number` | |
| `float` | `number` | |
| `bool` | `boolean` | |
| `Optional[str]` | `string \| undefined` 或 `description?` | |
| `List[Item]` | `Item[]` | |

**原则**：后端 Pydantic 模型 ≈ 前端的 interface；改 API 时两边一起改。

---

## 5. CORS：为什么本地要配？

浏览器**安全策略**：`http://localhost:5173` 的页面默认不能随意请求 `http://localhost:8000`，除非后端明确允许（CORS）。

本仓库在 `python-project-demo/app/main.py` 中已配置：

```python
origins = ["http://localhost:5173", "http://localhost:3000"]
app.add_middleware(CORSMiddleware, allow_origins=origins, ...)
```

开发时也可在 `react-frontend-demo/vite.config.ts` 用 **代理** 把 `/api` 转到 8000，减少跨域问题（见该文件注释）。

---

## 6. 动手实验（建议按顺序）

### 实验 A：只用 Swagger（不涉及前端）

1. 启动后端：`cd python-project-demo && python manage.py dev`
2. 打开 http://localhost:8000/docs
3. 对 `POST /api/v1/items/` 点 Try it out，填 JSON，Execute
4. 再 `GET /api/v1/items/` 看列表

此时你扮演的是「前端」——只是用网页代替 React。

### 实验 B：用 Python 当客户端

```bash
cd 13_fullstack_bridge
python 01_http_client.py
```

（需先启动后端。脚本用 `httpx` 发与 axios 相同的请求。）

### 实验 C：React 全链路

```bash
# 终端 1
cd python-project-demo && source venv/bin/activate && python manage.py dev

# 终端 2
cd react-frontend-demo && npm run dev
```

打开 http://localhost:5173 ，打开开发者工具 Network，点创建 Item，观察：

- Request URL、Method、Request Payload
- Response 状态码与 JSON

### 实验 D：对照读代码

| 步骤 | 前端文件 | 后端文件 |
|------|----------|----------|
| 发 POST | `src/lib/api.ts` | `app/api/v1/endpoints/items.py` → `create_new_item` |
| 校验 body | （TypeScript 编译期） | `app/schemas/item.py` → `ItemCreate` |
| 写库 | — | `app/crud/item.py` → `create_item` |
| 表结构 | — | `app/models/item.py` |

更细的调用图：`python-project-demo/docs/project-call-flow.md`。

---

## 7. 从 CLI Todo 迁移到 API 的思维转换

**CLI Todo**（`09_practical_example.py`）：

```python
# 用户输入 → 改内存列表 → 整文件写回 todos.json
manager.save()
```

**REST API**：

```python
# 一次 HTTP 请求只做一件事；每次 POST 只创建一条，由数据库持久化
@router.post("/")
def create_new_item(item: ItemCreate, db: Session = Depends(get_db)):
    return create_item(db=db, item=item)
```

| CLI | REST |
|-----|------|
| `python todo.py add 任务` | `POST /items` + JSON body |
| `python todo.py list` | `GET /items` |
| `python todo.py done 1` | `PUT /items/1` 更新 `is_active` |
| 一个进程、交互式 | 无状态请求，可多客户端（网页、App、脚本） |

---

## 8. 常见问题

**Q: 前端显示 Failed to fetch / CORS？**  
A: 确认后端已启动；检查 `main.py` 的 `origins` 是否包含你的前端端口。

**Q: 404 Not Found？**  
A: 注意路径前缀是 `/api/v1/items/`，不是 `/items`。

**Q: 422 Unprocessable Entity？**  
A: 请求体不符合 Pydantic 规则（如 `price` 必须是大于 0 的数字）。

**Q: Next.js 示例为什么请求 jsonplaceholder？**  
A: `nextjs-shadcn` 演示的是 Next 服务端请求；与 FastAPI 联调请参考 `react-frontend-demo`。

---

## 9. 学完后的自检清单

- [ ] 能解释 GET/POST/PUT/DELETE 在本项目里各对应什么操作
- [ ] 能说出 JSON 从前端表单到数据库表经过了哪几层
- [ ] 能在 Swagger 里手动完成 CRUD
- [ ] 能在 React 里完成同样 CRUD 并看懂 Network 面板
- [ ] 能对照修改 `schemas/item.py` 与 `types/index.ts` 并保持一致

---

**上一阶段**：[09_practical_example.py](./09_practical_example.py)  
**下一阶段**：`python-project-demo` + `react-frontend-demo`  
**练习**：[EXERCISES.md](./EXERCISES.md) 第 13 章
