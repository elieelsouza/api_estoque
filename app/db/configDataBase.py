import mariadb
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db = SQLAlchemy()

dbConnect = mariadb.connect(
    host="127.0.0.1",
    user="root",
    password="123456",
    database="db.development_cra",
    port=3306
)

engine = create_engine(
    "mariadb+mariadbconnector://root:123456@127.0.0.1:3306/db.development_cra")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
# Base.metadata.create_all(engine)
