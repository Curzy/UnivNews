from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///./database.sqlite')
Base = declarative_base()
db = sessionmaker(bind=engine)()