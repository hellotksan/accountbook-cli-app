# 家計簿アプリケーション

## Dumping Database

### Loginning MySQL terminal

```bash
mysql -u root -p
```

### Dumping DB file

```sql
SOURCE /path/to/your/project/db/db_schema.sql
SOURCE /path/to/your/project/db/accountbook.dmp
```

### Installing Python Modules

```bash
pip install -r requirements.txt
```

### Starting Fast API Server

```bash
uvicorn app/accountbook_api:app --reload
```

### python ファイルでアプリケーションを実行する

```bash
python.exe /path/to/your/project/app/crud/accountbook.py
```

## Folder Influstructure

```bash
├── accountbook/
│   ├── requirements.txt
│   ├── app/
│   │   ├── crud/  # pythonのCLIアプリ
│   │   │   ├── accountbook.py  # 家計簿アプリケーションのメインファイル
│   │   │   ├── accountbook_register.py  # 家計簿アプリの登録モジュール
│   │   │   ├── ...
│   │   │   ├── input_utils.py  # 共通の入力処理を提供するモジュール群
│   │   ├── dbaccess.py  # FastAPIのエントリーポイント兼エンドポイント
│   ├── db/
│   │   ├── accountbook.dmp  # accountbookデータベースのdmpファイル
│   │   ├── db_schema.sql  # データベースのスキーマ定義SQLファイル
│   │   ├── dummydata.sql  # ダミーデータのSQLファイル
│   ├── docs/
│   │   ├── 2024-08-27 17-44-54.mkv  # 実際に使用している模擬動画(Python)
│   │   ├── 2024-08-28 21-11-57.mkv  # 実際に使用している模擬動画(NextJs)
│   │   ├── 単体テスト項目書.xlsx  # 単体テスト項目書
```
