import logging

from sqlalchemy.orm import sessionmaker

from DAL import DBConnector
from ENV import Env

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)


def db_writer(model: object):
    db_session: sessionmaker = DBConnector.create_db_session(Env.DBName.MSSQLSERVER)
    new_session = db_session()
    new_session.add(model)
    new_session.commit()
    new_session.close()
