QooQQloud/
├── .venv/                        
├── db/
│   ├── crud.py                   # Database operations, including CRUD for students, classes, and record logs
│   ├── database.py               # Database connection settings and initialization
│   ├── models.py                 # Defines all database models, including Student, Class, and RecordLog
├── routers/
│   ├── class_routes.py           # Routes for class-related APIs
│   ├── student_routes.py         # Routes for student-related APIs
│   ├── recordlog_routes.py       # Routes for record log-related APIs (new)
├── schemas/
│   ├── class_schema.py           # Pydantic schema for classes
│   ├── student_schema.py         # Pydantic schema for students
│   ├── recordlog_schema.py       # Pydantic schema for record logs (new)
├── main.py                       # FastAPI application entry point, includes all routes



- QooQCloud/
  - .idea/                       # PyCharm 專案設定（建議忽略）
  - .gitignore                   # Git 忽略清單
  - main.py                      # FastAPI 應用進入點
  - Readme.md                    # 專案說明文件
  - app/
    - api/
      - V1/
        - auth.py               # 使用者驗證與登入邏輯
        - class_routes.py       # 課程 API
        - record_logs.py        # 紀錄 API
        - student_routes.py     # 學生 API
        - users_route.py        # 使用者管理 API
        - validate.py           # 輸入驗證模組
    - db/
      - database.py             # 資料庫連線設定
      - db_connect_test.py      # DB 測試程式
    - models/
      - models.py               # SQLAlchemy 資料模型
    - schemas/
      - class_schema.py         # 課程資料結構
      - student_schema.py       # 學生資料結構
      - user_schemas.py         # 使用者資料結構
