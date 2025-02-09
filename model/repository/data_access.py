from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from model.entity.base import Base

# تنظیمات اتصال به دیتابیس
connection_string = "mysql+pymysql://root:@localhost/apm"
if not database_exists(connection_string):
    create_database(connection_string)

# ایجاد موتور و ارتباط با دیتابیس
engine = create_engine(connection_string)
Base.metadata.create_all(engine)

# ساخت سشن برای انجام عملیات روی دیتابیس
Session = sessionmaker(bind=engine)
session = Session()

# کلاس مدیریت عملیات دیتابیس با استفاده از SQLAlchemy
class Database:
    def __init__(self, class_name):
        self.class_name = class_name

    def save(self, entity):
        session.add(entity)
        session.commit()
        session.refresh(entity)
        return entity

    def edit(self, entity):
        session.merge(entity)
        session.commit()
        return entity

    def remove(self, entity):
        session.delete(entity)
        session.commit()
        return entity

    def remove_by_id(self, entity_id):
        entity = session.get(self.class_name, entity_id)
        if entity:
            session.delete(entity)
            session.commit()
            return entity
        return None

    def find_all(self):
        return session.query(self.class_name).all()

    def find_by_id(self, id):
        return session.get(self.class_name, id)

    def find_by(self, find_statement):
        return session.query(self.class_name).filter(find_statement).all()

    def close_session(self):
        session.close()
