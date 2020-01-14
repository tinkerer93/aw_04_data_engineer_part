import os
import sqlalchemy as sqla
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class ParsedData(Base):
    __tablename__ = 'parsed_data'

    id = Column(Integer, primary_key=True)
    entity = Column(String)
    value = Column(Float)
    string = Column(String)


def create_db(filepath, db_name):
    engine = sqla.create_engine('sqlite:///' + os.path.join(filepath, db_name), encoding='utf-8')
    Base.metadata.create_all(engine)
