import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class VersionTable(Base):
    __tablename__ = 'versionTable'

    version = Column(Integer, primary_key=True)


class Table1(Base):
    __tablename__ = 'table1'
    id = Column(Integer, primary_key=True)
    col1 = Column(String(250))
    col2 = Column(String(250))

engine = create_engine('mysql://root:password@localhost/test')
Base.metadata.create_all(engine)




