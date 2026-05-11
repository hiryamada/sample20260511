"""Hello World APIエンドポイントの単体テストモジュール。"""

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_root_status_code():
    """ルートエンドポイントが200 OKを返すことを確認するテスト。"""
    response = client.get("/")
    assert response.status_code == 200


def test_read_root_response_body():
    """ルートエンドポイントが正しいHello Worldメッセージを返すことを確認するテスト。"""
    response = client.get("/")
    assert response.json() == {"message": "Hello World"}
