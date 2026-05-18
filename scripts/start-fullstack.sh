#!/usr/bin/env bash
# 一键启动 FastAPI 后端 + React 前端（需分别在两个终端查看日志时，可只运行本脚本）
set -e
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

echo ">>> 启动 FastAPI 后端 (http://localhost:8000)"
echo ">>> 启动 React 前端 (http://localhost:5173)"
echo ">>> 文档: $ROOT/FULLSTACK_GUIDE.md"
echo ""

cd "$ROOT/python-project-demo"
if [ ! -d "venv" ]; then
  echo "正在创建虚拟环境..."
  python3 -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
else
  source venv/bin/activate
fi

# 后台启动 API
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000 &
BACKEND_PID=$!

cd "$ROOT/react-frontend-demo"
if [ ! -d "node_modules" ]; then
  npm install
fi

cleanup() {
  echo ""
  echo "正在停止后端 (pid $BACKEND_PID)..."
  kill "$BACKEND_PID" 2>/dev/null || true
}
trap cleanup EXIT INT TERM

npm run dev
