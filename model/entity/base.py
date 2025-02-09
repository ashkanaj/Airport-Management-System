from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String, Float, Boolean
from datetime import datetime

DATABASE_URL = "mysql+mysqlconnector://root:1234Abcd@localhost:3306/apm"

engine = create_engine(DATABASE_URL, echo=True)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = Session()


class Base(declarative_base()):
    __abstract__ = True

    def __repr__(self):
        return str({c.name: getattr(self, c.name) for c in self.__table__.columns})

    @classmethod
    def save(cls, session):

        if not cls.id:
            session.add(cls)
        session.commit()

    @classmethod
    def delete(cls, session):

        session.delete(cls)
        session.commit()

    @classmethod
    def update(cls, session, updates):

        for field, value in updates.items():
            setattr(cls, field, value)
        session.commit()


class Passenger(Base):
    __tablename__ = 'passengers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    is_checked_in = Column(Boolean, default=False)

