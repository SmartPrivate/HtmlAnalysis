from sqlalchemy import Column, NVARCHAR, Integer, TEXT, DATETIME, BOOLEAN
from sqlalchemy.ext.declarative import declarative_base

import logging

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)

Base = declarative_base()


class WeChatContent(Base):
    __tablename__ = 'T_WeChatContent'

    SID = Column(Integer, primary_key=True)
    QueryKeyword = Column(NVARCHAR(20))
    PostUserName = Column(NVARCHAR(50))
    PostUserID = Column(NVARCHAR(50))
    Title = Column(NVARCHAR(200))
    PostDate = Column(DATETIME)
    OriginTag = Column(BOOLEAN)
    URL = Column(TEXT)
    Article = Column(TEXT)


class IpPoolContent(Base):
    __tablename__ = 'T_IPPool'

    SID = Column(Integer, primary_key=True)
    IP = Column(NVARCHAR(20))
    PORT = Column(Integer)
    IPArea = Column(NVARCHAR(20))
    IPModel = Column(NVARCHAR(5))
    IPType = Column(NVARCHAR(5))


class SNUIDPoolContent(Base):
    __tablename__ = 'T_SNUIDPool'

    SID = Column(Integer, primary_key=True)
    SUID = Column(NVARCHAR(50))
    SNUID = Column(NVARCHAR(50))
