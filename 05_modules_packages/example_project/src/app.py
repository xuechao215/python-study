#!/usr/bin/env python3
"""
示例应用 - 演示虚拟环境和依赖管理
"""

import os
import sys
from datetime import datetime
from typing import Optional

import requests
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from loguru import logger

# 加载环境变量
load_dotenv()

# 配置日志
logger.remove()  # 移除默认处理器
logger.add(
    sys.stderr,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    level="INFO",
)

# 创建 Flask 应用
app = Flask(__name__)

# 配置 JSON 响应不转义中文字符
app.config['JSON_AS_ASCII'] = False


class Config:
    """应用配置"""
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")
    API_TIMEOUT = int(os.getenv("API_TIMEOUT", "30"))


app.config.from_object(Config)


@app.route("/")
def index():
    """首页 - 返回 HTML 页面"""
    from flask import render_template
    return render_template('index.html')

@app.route("/api/info")
def app_info():
    """应用信息 API"""
    import json
    from flask import Response
    data = {
        "message": "欢迎使用 Python 虚拟环境示例应用",
        "timestamp": datetime.now().isoformat(),
        "python_version": sys.version,
        "virtual_env": os.getenv("VIRTUAL_ENV", "未检测到虚拟环境"),
    }
    return Response(
        json.dumps(data, ensure_ascii=False),
        mimetype='application/json; charset=utf-8'
    )


@app.route("/health")
def health_check():
    """健康检查端点"""
    import json
    from flask import Response
    data = {"status": "healthy", "timestamp": datetime.now().isoformat()}
    return Response(
        json.dumps(data, ensure_ascii=False),
        mimetype='application/json; charset=utf-8'
    )


@app.route("/api/external")
def external_api():
    """调用外部 API 示例"""
    import json
    from flask import Response
    url = "https://api.github.com"

    try:
        response = requests.get(url, timeout=app.config["API_TIMEOUT"])
        response.raise_for_status()

        data = {
            "status": "success",
            "url": url,
            "status_code": response.status_code,
            "response_time": response.elapsed.total_seconds(),
        }
        return Response(
            json.dumps(data, ensure_ascii=False),
            mimetype='application/json; charset=utf-8'
        )
    except requests.exceptions.RequestException as e:
        logger.error(f"调用外部 API 失败: {e}")
        data = {"status": "error", "message": str(e)}
        return Response(
            json.dumps(data, ensure_ascii=False),
            mimetype='application/json; charset=utf-8',
            status=500
        )


@app.route("/api/echo", methods=["POST"])
def echo():
    """回显请求数据"""
    import json
    from flask import Response
    data = request.get_json() or {}

    response_data = {
        "message": "收到数据",
        "timestamp": datetime.now().isoformat(),
        "data": data,
        "headers": dict(request.headers),
    }
    return Response(
        json.dumps(response_data, ensure_ascii=False),
        mimetype='application/json; charset=utf-8'
    )


def check_environment() -> bool:
    """检查运行环境"""
    # 检查是否在虚拟环境中
    in_venv = os.getenv("VIRTUAL_ENV") is not None

    if not in_venv:
        logger.warning("⚠️  未检测到虚拟环境！建议使用虚拟环境运行此应用。")
        logger.warning("   创建虚拟环境: python -m venv venv")
        logger.warning("   激活虚拟环境: source venv/bin/activate (macOS/Linux)")
        logger.warning("                  venv\\Scripts\\activate (Windows)")

    # 检查依赖
    try:
        import flask
        import requests
        import loguru
        logger.info("✅ 所有依赖已正确安装")
        return True
    except ImportError as e:
        logger.error(f"❌ 缺少依赖: {e}")
        logger.info("   安装依赖: pip install -r requirements.txt")
        return False


def main():
    """主函数"""
    logger.info("=" * 50)
    logger.info("启动 Python 虚拟环境示例应用")
    logger.info("=" * 50)

    # 检查环境
    if not check_environment():
        logger.error("环境检查失败，应用无法启动")
        sys.exit(1)

    # 显示配置信息
    logger.info(f"应用配置:")
    logger.info(f"  - DEBUG: {app.config['DEBUG']}")
    logger.info(f"  - API_TIMEOUT: {app.config['API_TIMEOUT']}s")
    logger.info(f"  - Python 版本: {sys.version}")
    logger.info(f"  - 虚拟环境: {os.getenv('VIRTUAL_ENV', '未激活')}")

    # 显示可用端点
    logger.info("可用端点:")
    for rule in app.url_map.iter_rules():
        if rule.endpoint != "static":
            logger.info(f"  - {rule.rule} ({', '.join(rule.methods)})")

    # 启动应用
    host = os.getenv("HOST", "127.0.0.1")
    port = int(os.getenv("PORT", "5000"))

    logger.info(f"启动服务器: http://{host}:{port}")
    logger.info("按 Ctrl+C 停止服务器")

    app.run(host=host, port=port, debug=app.config["DEBUG"])


if __name__ == "__main__":
    main()
    print("应用启动完成")