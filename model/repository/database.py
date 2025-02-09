# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from model.entity.base import Base


connection_string = "mysql+pymysql://root:@localhost/apm"
if not database_exists(connection_string):
    create_database(connection_string)


engine = create_engine(connection_string)
Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()
