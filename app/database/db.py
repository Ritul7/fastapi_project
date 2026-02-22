from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine
from app.config.app_config import AppConfig
from typing import Generator

Base = declarative_base()

config = AppConfig()
engine = create_engine(config.database_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try: 
        yield db                    # safe connection handling
    finally:
        db.close()


# Declarative Base - Without this, python classes ko database tables ke sath map nhi kiya jaa skta
# Engine is like connection manager to postgresql, connects fastAPI with postgreSQL
# Appconfig - This imports configuration class which loads .env, instead of hardcoding the db url
# Base tells SQLAlchemy, this class represents a database table
# autocommit - (false) it means, we have to manually add db.commit()
# autoflush - It sends automatic sending changes to the database

# Alembic manages: Schema changes,Table updates,Column additions,Column deletions,Index changes,Constraints
# psycopg2 is a database adpter/driver that allows SQLAlchemy/Python app to communicate with PostgreSQL.




