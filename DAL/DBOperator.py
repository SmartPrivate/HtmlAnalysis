import logging

from sqlalchemy.orm import sessionmaker

from DAL import DBConnector
from ENV import Env
from MODEL import OrmData

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)


def db_writer(model: object):
    db_session: sessionmaker = DBConnector.create_db_session(Env.DBName.MSSQLSERVER)
    new_session = db_session()
    new_session.add(model)
    new_session.commit()
    new_session.close()


def db_select_ip_address() -> [OrmData.IpPoolContent]:
    db_session: sessionmaker = DBConnector.create_db_session(Env.DBName.MSSQLSERVER)
    new_session = db_session()
    ip_pool = new_session.query(OrmData.IpPoolContent)
    return ip_pool


def db_select_snuid() -> [OrmData.SNUIDPoolContent]:
    db_session: sessionmaker = DBConnector.create_db_session(Env.DBName.MSSQLSERVER)
    new_session = db_session()
    snuid_pool = new_session.query(OrmData.SNUIDPoolContent)
    return snuid_pool
