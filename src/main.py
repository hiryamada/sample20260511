"""FastAPIを使用したHello Worldアプリケーションのメインモジュール。"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root() -> dict:
    """ルートエンドポイントのハンドラ。

    Returns:
        dict: "Hello World"メッセージを含む辞書。
    """
    return {"message": "Hello World"}
