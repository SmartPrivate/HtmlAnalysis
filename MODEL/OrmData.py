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


class SoftwareCopyrightContent(Base):
    __tablename__ = 'T_SoftwareCopyright'

    SID = Column(Integer, primary_key=True)
    URL = Column(NVARCHAR(100))
    CopyrightName = Column(NVARCHAR(100))
    CopyrightID = Column(NVARCHAR(20))
    CompanyName = Column(NVARCHAR(100))
    RegistrationDate = Column(DATETIME)
    Notes = Column(TEXT)


class SoftwareCopyrightDateUrlContent(Base):
    __tablename__ = 'T_SoftwareCopyrightDateUrl'

    SID = Column(Integer, primary_key=True)
    DateURL = Column(NVARCHAR(50))


class UserAgentContent(Base):
    __tablename__ = 'D_UserAgent'

    SID = Column(Integer, primary_key=True)
    UserAgent = Column(TEXT)