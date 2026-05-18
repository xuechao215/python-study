# 请求链路：React 与 FastAPI 并排对照

以 **创建一条 Item** 为例。

## 前端（TypeScript）

```typescript
// react-frontend-demo/src/lib/api.ts
await api.post<Item>('/items/', {
  title: 'MacBook',
  price: 1999,
  description: '笔记本',
});
```

## 后端（Python）

```python
# python-project-demo/app/api/v1/endpoints/items.py
@router.post("/", response_model=Item, status_code=201)
async def create_new_item(item: ItemCreate, db: Session = Depends(get_db)):
    return create_item(db=db, item=item)
```

## 网络上实际发生的事

```http
POST /api/v1/items/ HTTP/1.1
Host: localhost:8000
Content-Type: application/json

{"title":"MacBook","price":1999,"description":"笔记本"}
```

响应示例：

```http
HTTP/1.1 201 Created
Content-Type: application/json

{"id":1,"title":"MacBook","price":1999.0,"description":"笔记本","tax":null,"is_active":true}
```

## 各层职责（背下来很有用）

| 层 | 前端 | 后端 |
|----|------|------|
| 展示 | `ItemForm.tsx` 表单 | — |
| 调用 | `api.ts` axios | `endpoints/items.py` 路由 |
| 契约 | `types/index.ts` | `schemas/item.py` Pydantic |
| 业务 | — | `crud/item.py` |
| 存储 | — | `models/item.py` + SQLite |

## 练习

1. 在 Swagger 创建一条 Item，记下 Request Body 和 Response。
2. 在 React 创建一条，在 DevTools → Network 找到同名字段对比。
3. 运行 `python 01_http_client.py`，对比三次请求体是否一致。
