# models.py
from sqlalchemy import Column, Integer, String
from .database import Base

class ExampleModel(Base):
    __tablename__ = 'example_table'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
