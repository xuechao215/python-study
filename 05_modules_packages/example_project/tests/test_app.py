"""
应用测试
"""

import json
from unittest.mock import patch

import pytest
from src.app import app, check_environment


@pytest.fixture
def client():
    """测试客户端"""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_index_endpoint(client):
    """测试首页端点"""
    response = client.get("/")
    assert response.status_code == 200

    data = json.loads(response.data)
    assert "message" in data
    assert "timestamp" in data
    assert "python_version" in data


def test_health_check(client):
    """测试健康检查端点"""
    response = client.get("/health")
    assert response.status_code == 200

    data = json.loads(response.data)
    assert data["status"] == "healthy"
    assert "timestamp" in data


def test_echo_endpoint(client):
    """测试回显端点"""
    test_data = {"message": "Hello", "number": 42}

    response = client.post(
        "/api/echo",
        data=json.dumps(test_data),
        content_type="application/json"
    )
    assert response.status_code == 200

    data = json.loads(response.data)
    assert data["message"] == "收到数据"
    assert data["data"] == test_data
    assert "headers" in data


@patch("src.app.requests.get")
def test_external_api_success(mock_get, client):
    """测试外部 API 调用成功"""
    # 模拟成功的响应
    mock_response = mock_get.return_value
    mock_response.status_code = 200
    mock_response.elapsed.total_seconds.return_value = 0.5

    response = client.get("/api/external")
    assert response.status_code == 200

    data = json.loads(response.data)
    assert data["status"] == "success"
    assert data["status_code"] == 200


@patch("src.app.requests.get")
def test_external_api_failure(mock_get, client):
    """测试外部 API 调用失败"""
    # 模拟失败的响应
    mock_get.side_effect = Exception("Connection failed")

    response = client.get("/api/external")
    assert response.status_code == 500

    data = json.loads(response.data)
    assert data["status"] == "error"


def test_check_environment():
    """测试环境检查函数"""
    # 这个测试可能会根据实际环境有所不同
    result = check_environment()
    # 我们只检查函数是否执行而不抛出异常
    assert isinstance(result, bool)


def test_app_config():
    """测试应用配置"""
    assert hasattr(app.config, "DEBUG")
    assert hasattr(app.config, "SECRET_KEY")
    assert hasattr(app.config, "API_TIMEOUT")


def test_invalid_endpoint(client):
    """测试无效端点"""
    response = client.get("/invalid")
    assert response.status_code == 404


class TestEnvironment:
    """环境相关测试"""

    def test_imports(self):
        """测试所有必要的导入"""
        import flask
        import requests
        import loguru
        from dotenv import load_dotenv

        # 如果这些导入成功，测试通过
        assert True

    def test_python_version(self):
        """测试 Python 版本"""
        import sys
        # 确保是 Python 3
        assert sys.version_info.major == 3
        # 建议使用 Python 3.7+
        assert sys.version_info.minor >= 7


if __name__ == "__main__":
    # 直接运行测试
    pytest.main([__file__, "-v"])