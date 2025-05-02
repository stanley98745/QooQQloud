from sqlalchemy import create_engine

# db: Qook_db
# Account:Qooktest;password:qooktest
# Port: 9487
DATABASE_URL = "postgresql://Qooktest:qooktest@localhost:9487/Qook_db"
engine = create_engine(DATABASE_URL)

# 測試連接
try:
    with engine.connect() as connection:
        print("Database connection successful!")
except Exception as e:
    print("Database connection failed:", e)