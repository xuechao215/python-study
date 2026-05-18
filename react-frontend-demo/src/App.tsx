import ItemList from './components/ItemList';

/**
 * 全栈演示入口：CRUD 在 ItemList + lib/api.ts
 * 后端: cd python-project-demo && python manage.py dev
 */
function App() {
  return (
    <div className="min-h-screen bg-gray-50">
      <header className="bg-white shadow-sm border-b border-gray-200">
        <div className="container mx-auto px-4 py-4 flex justify-between items-center">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 bg-blue-600 rounded-lg flex items-center justify-center text-white font-bold text-xl shadow-md">
              Py
            </div>
            <h1 className="text-xl font-bold text-gray-900 tracking-tight">
              Python + React 全栈演示
            </h1>
          </div>
          <a
            href="http://localhost:8000/docs"
            target="_blank"
            rel="noopener noreferrer"
            className="text-sm font-medium text-gray-600 hover:text-blue-600 transition-colors"
          >
            后端 Swagger 文档 →
          </a>
        </div>
      </header>

      <main className="container mx-auto px-4 py-8">
        <p className="text-sm text-gray-600 mb-6 max-w-2xl">
          本页通过 HTTP 调用 FastAPI。打开开发者工具 Network 可看到 GET/POST/PUT/DELETE 与 JSON 响应。
        </p>
        <ItemList />
      </main>
    </div>
  );
}

export default App;
