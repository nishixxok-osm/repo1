# FastAPI Hello World プロジェクト

シンプルなFastAPI アプリケーションです。Hello Worldエンドポイントを提供し、pytestを使用した単体テストを含みます。
2026/5/7

## プロジェクト構成

```
repo1/
├── src/
│   ├── __init__.py
│   └── main.py          # FastAPI アプリケーション
├── tests/
│   ├── __init__.py
│   └── test_main.py     # pytest テストファイル
├── requirements.txt     # 依存パッケージ
└── README.md
```

## インストール

```bash
pip install -r requirements.txt
```

## 実行

### テストの実行

```bash
pytest tests/
```

### サーバーの起動

```bash
uvicorn src.main:app --reload
```

サーバーは `http://localhost:8000` で起動します。

## API エンドポイント

### GET /

```json
{
  "message": "Hello World"
}
```

### GET /hello

```json
{
  "message": "Hello World"
}
```

## テスト

プロジェクトには以下のテストが含まれています：

- `test_read_root()` - GET / エンドポイントのテスト
- `test_read_hello()` - GET /hello エンドポイントのテスト
- `test_response_type()` - レスポンスデータ型の検証
