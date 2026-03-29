import { Button } from '@/components/ui/button'
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from '@/components/ui/card'
import request from '@/lib/request'

interface Todo {
  userId: number
  id: number
  title: string
  completed: boolean
}

export default async function Home() {
  let todo: Todo | null = null
  let errorMsg = ''

  try {
    // 这里的 get 返回的是 response.data，因为拦截器处理了
    // 假设 request.get 已经返回 T 类型的数据
    // 注意：request.ts 中拦截器直接返回了 response.data
    // 如果是服务端组件，可以直接调用
    // JSONPlaceholder 返回的是直接的对象
    const data = await request.get<Todo>('/todos/1')
    todo = data
  } catch (error) {
    errorMsg = '获取数据失败'
    console.error(error)
  }

  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-8 gap-8">
      <Card className="w-full max-w-md">
        <CardHeader>
          <CardTitle>Next.js + shadcn/ui</CardTitle>
          <CardDescription>已就绪</CardDescription>
        </CardHeader>
        <CardContent>
          <p className="text-sm text-muted-foreground mb-4">这是使用 shadcn/ui 的示例。</p>
          
          <div className="p-4 border rounded-md bg-muted/50">
            <h3 className="font-semibold mb-2">Axios 请求测试:</h3>
            {todo ? (
              <div className="space-y-1 text-sm">
                <p><span className="font-medium">ID:</span> {todo.id}</p>
                <p><span className="font-medium">Title:</span> {todo.title}</p>
                <p><span className="font-medium">Status:</span> {todo.completed ? 'Completed' : 'Pending'}</p>
              </div>
            ) : (
              <p className="text-destructive text-sm">{errorMsg || 'Loading...'}</p>
            )}
          </div>
        </CardContent>
        <CardFooter>
          <Button>开始使用</Button>
        </CardFooter>
      </Card>
    </main>
  )
}
