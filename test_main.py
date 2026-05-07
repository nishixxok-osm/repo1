import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestHelloWorldAPI:
    """Hello World API のテストクラス"""

    def test_read_root(self):
        """GET / エンドポイントのテスト"""
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello World"}

    def test_read_hello(self):
        """GET /hello エンドポイントのテスト"""
        response = client.get("/hello")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello World"}

    def test_response_type(self):
        """レスポンスのデータ型が正しいかテスト"""
        response = client.get("/")
        data = response.json()
        assert isinstance(data, dict)
        assert isinstance(data["message"], str)
