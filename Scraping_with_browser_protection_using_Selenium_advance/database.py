from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool


DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/TASK2"


engine = create_engine(DATABASE_URL, pool_size=50)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
