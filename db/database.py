from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from databases import Database


# URL Link for Qook-Qloud Database
# db: Qook_db
# Account:Qooktest;password:qooktest
# Port: 9487
DATABASE_URL = "postgresql://Qooktest:qooktest@localhost:9487/Qook_db"

# Create engine and session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def initialize_database():
    """Initialize the database and create all tables"""
    Base.metadata.create_all(bind=engine)
    print("Database initialized")

def get_database_session():
    """Retrieve a database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()