from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime
from sqlalchemy.orm import declarative_base
Base = declarative_base()

DATABASE_URL = "mysql+mysqlconnector://root:1234Abcd@localhost:3306/apm"

engine = create_engine(DATABASE_URL, echo=True)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = Session()


class Base(declarative_base()):
    __abstract__ = True

    def __repr__(self):
        return str({c.name: getattr(self, c.name) for c in self.__table__.columns})


class Passenger(Base):
    __tablename__ = 'passengers'

    id = Column(Integer, primary_key=True, autoincrement=True)  # اضافه کردن autoincrement
    name = Column(String(255), index=True)  # اضافه کردن طول 255 به نوع String
    age = Column(Integer)
    is_checked_in = Column(Boolean, default=False)


Base.metadata.create_all(bind=engine)

new_passenger = Passenger(name="John Doe", age=30)

session.add(new_passenger)
session.commit()

new_passenger.age = 31
session.commit()

session.delete(new_passenger)
session.commit()

passenger_to_delete = session.query(Passenger).filter(Passenger.name == "John Doe").first()
if passenger_to_delete:
    session.delete(passenger_to_delete)
    session.commit()

session.close()
