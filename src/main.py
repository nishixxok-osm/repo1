from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    """Root エンドポイント - Hello World を返す"""
    return {"message": "Hello World"}


@app.get("/hello")
def read_hello():
    """Hello エンドポイント - Hello World を返す"""
    return {"message": "Hello World"}
