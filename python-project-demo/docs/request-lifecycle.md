# python-project-demo 请求执行顺序讲解

这份文档专门回答一个初学者最常见的问题：

**当前端发出一个请求后，这个 Python 项目内部到底是怎么一步一步执行的？**

我们用“创建一个 item”这条请求来讲最容易理解。

---

## 1. 示例请求

假设你发送这样一个请求：

```http
POST /api/v1/items/
Content-Type: application/json

{
  "title": "Book",
  "description": "Python book",
  "price": 99.9
}
```

这个请求的目标是：
**创建一条新的 item 数据。**

---

## 2. 执行顺序总览

先看一张简化图：

```text
客户端发请求
   ↓
app/main.py
   ↓
app/api/v1/api.py
   ↓
app/api/v1/endpoints/items.py
   ↓
app/schemas/item.py 校验请求体
   ↓
app/db/session.py 提供 db
   ↓
app/crud/item.py 执行数据库写入
   ↓
app/models/item.py 映射到数据表
   ↓
SQLite 数据库
   ↓
返回结果给路由
   ↓
FastAPI 按 response_model 输出 JSON
   ↓
客户端收到响应
```

---

## 3. 逐步讲解

### 第 1 步：请求进入 FastAPI 应用

入口文件是：`app/main.py`

这里创建了：

```python
app = FastAPI(...)
```

也就是说，整个 Web 服务是从这里启动的。

同时它还做了这件事：

```python
app.include_router(api_router, prefix=settings.API_V1_STR)
```

这表示：
- 把总路由注册进来
- 给所有接口统一加上 `/api/v1` 前缀

所以客户端请求 `/api/v1/items/` 时，FastAPI 能知道应该交给哪组路由处理。

---

### 第 2 步：进入总路由分发器

接下来会进入：`app/api/v1/api.py`

这个文件里有：

```python
api_router.include_router(items.router, prefix="/items", tags=["Items"])
```

它的作用是：
- 把 items 模块挂到 `/items`

再和上一步的 `/api/v1` 组合起来，就形成了完整路径：

```text
/api/v1/items
```

这一层不做具体业务，只负责“把请求分发到正确的模块”。

---

### 第 3 步：进入具体接口函数

然后会进入：`app/api/v1/endpoints/items.py`

创建接口对应的是：

```python
@router.post("/", response_model=Item, status_code=status.HTTP_201_CREATED)
async def create_new_item(...):
```

这里定义了：
- 请求方法是 `POST`
- 路径是 `/`
- 返回结构用 `Item`
- 成功状态码是 `201`

你可以把这里理解成：
**真正接住这个 HTTP 请求的地方。**

---

### 第 4 步：FastAPI 校验请求体

接口函数参数里有这样一项：

```python
item: ItemCreate
```

这里的 `ItemCreate` 来自：`app/schemas/item.py`

这意味着 FastAPI 会自动把客户端发来的 JSON 按 `ItemCreate` 进行校验。

比如它会检查：
- `title` 是否存在
- `price` 是否存在
- `price` 是否大于 0
- 字段类型是否正确

如果数据不合法，FastAPI 不会继续往下执行，而是直接返回错误。

例如：
- 少传 `title`
- `price` 传成负数
- `price` 传成字符串但无法转换

这一步就是：
**先保证输入数据合法。**

---

### 第 5 步：FastAPI 自动准备数据库会话

接口参数里还有：

```python
db: Session = Depends(get_db)
```

这里的 `get_db` 来自：`app/db/session.py`

它的意思是：
- 这个接口运行前
- FastAPI 先执行 `get_db()`
- 拿到一个数据库会话 `db`
- 再把这个 `db` 传给接口函数

你可以理解成：
**框架提前帮你准备好了数据库操作工具。**

当请求结束后，这个会话还会被关闭。

---

### 第 6 步：路由调用 CRUD 层

在接口函数内部，会调用：

```python
return create_item(db=db, item=item)
```

这就进入了：`app/crud/item.py`

这一层开始真正处理数据库逻辑。

这一步的意义是：
路由层负责“接请求”，CRUD 层负责“操作数据”，两者分工明确。

---

### 第 7 步：CRUD 层创建 ORM 对象

在 `create_item()` 中，会做类似下面这些事：

```python
db_item = Item(
    title=item.title,
    description=item.description,
    price=item.price,
    tax=item.tax,
    is_active=True
)
```

这里的 `Item` 来自：`app/models/item.py`

这个 `Item` 不是接口 schema，而是数据库 ORM 模型。

它对应数据库中的 `items` 表。

这一层做的是：
**把经过校验的数据，转换成数据库模型对象。**

---

### 第 8 步：把数据写入数据库

接着 CRUD 层会执行：

```python
db.add(db_item)
db.commit()
db.refresh(db_item)
```

这三步可以这样理解：

#### `db.add(db_item)`
把这个对象加入当前数据库会话，准备写入。

#### `db.commit()`
真正提交到数据库。

#### `db.refresh(db_item)`
从数据库重新读取这条记录，这样像 `id` 这种数据库自动生成的字段也会更新到对象里。

执行完以后，这条数据就真的进入数据库了。

---

### 第 9 步：CRUD 返回结果给路由层

写入成功后，`create_item()` 会返回 `db_item`。

这个对象会回到：
- `app/api/v1/endpoints/items.py`

也就是从 CRUD 层回到路由层。

---

### 第 10 步：FastAPI 按响应模型生成 JSON

虽然返回的是 ORM 对象，但接口上声明了：

```python
response_model=Item
```

这里的 `Item` 是 `app/schemas/item.py` 里的响应模型。

FastAPI 会根据这个响应模型，把 ORM 对象转换成规范的 JSON。

也就是说，客户端不会直接看到数据库对象本身，而是会看到一个符合接口约定的响应结果。

例如：

```json
{
  "title": "Book",
  "description": "Python book",
  "price": 99.9,
  "tax": null,
  "id": 1,
  "is_active": true
}
```

---

### 第 11 步：响应返回给客户端

最后，客户端收到：
- 状态码 `201`
- JSON 数据

这表示创建成功。

如果你是在 Swagger 页面测试，就会直接看到这份响应。

---

## 4. 如果请求失败，会在哪一步失败？

这对初学者也很重要。

### 情况 1：请求参数不合法
会在 **schema 校验阶段** 失败。

例如：
- 缺少 `title`
- `price <= 0`

结果：FastAPI 直接返回 422。

---

### 情况 2：访问不存在的数据
会在 **路由 + CRUD 查询结果判断** 这里失败。

例如：
- `GET /api/v1/items/999`
- 数据库查不到

代码会抛出：

```python
HTTPException(status_code=404, detail="Item not found")
```

结果：返回 404。

---

### 情况 3：数据库写入出问题
会在 **CRUD 提交数据库** 的阶段失败。

这个示例项目没有展开很多错误处理，但真实项目里通常会在这里做更多异常处理。

---

## 5. 用一句话总结这次请求的生命周期

你可以把整个过程记成一句话：

> 客户端发请求后，FastAPI 先找到对应路由，再用 schema 校验数据，接着注入数据库会话，随后由 CRUD 层操作 ORM 模型写入数据库，最后按响应模型返回 JSON 给客户端。

---

## 6. 初学者最容易混淆的三个点

### 6.1 `schemas.Item` 和 `models.Item` 不是一回事

- `schemas.Item`：接口层的数据结构
- `models.Item`：数据库层的数据结构

一个面向 API，一个面向数据库。

---

### 6.2 路由层不是数据库层

路由层主要负责：
- 接请求
- 校验参数
- 调用下层
- 返回结果

真正查库、写库的是 CRUD 层。

---

### 6.3 `Depends(get_db)` 不是手动调用

你没有在接口里手动写：

```python
db = get_db()
```

因为这是 FastAPI 的依赖注入机制自动完成的。

---

## 7. 建议你怎么自己跟代码读一遍

你可以按下面顺序打开代码：

1. `app/main.py`
2. `app/api/v1/api.py`
3. `app/api/v1/endpoints/items.py`
4. `app/schemas/item.py`
5. `app/crud/item.py`
6. `app/models/item.py`
7. `app/db/session.py`

然后只盯着“创建 item”这一条路径去看。

这样比一下子把全项目全看完，更容易建立理解。
