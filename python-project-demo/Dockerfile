# 使用官方 Python 运行时作为父镜像
# slim 版本更小，适合生产环境
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 设置环境变量
# PYTHONDONTWRITEBYTECODE 1: 防止 Python 写入 .pyc 文件
# PYTHONUNBUFFERED 1: 确保 Python 输出直接发送到终端 (不缓冲)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 安装系统依赖 (如果需要编译某些 Python 包)
# RUN apt-get update && apt-get install -y --no-install-recommends gcc

# 复制依赖文件
COPY requirements.txt .

# 安装依赖
# --no-cache-dir: 不缓存包，减小镜像体积
RUN pip install --no-cache-dir -r requirements.txt

# 复制项目代码
COPY . .

# 暴露端口
EXPOSE 8000

# 启动命令
# 使用 uvicorn 启动应用
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
