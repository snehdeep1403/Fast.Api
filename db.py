from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#Connection String
DB_URL = "mysql+pymysql://dbuser:password@localhost/testdb"

#Initialize db engine
engine = create_engine(DB_URL)

#Creates session obejct. 
SessionLocal = sessionmaker(bind=engine)

#Base class that would be used to create models
Base = declarative_base()

# Dependency function to create local session to database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()