from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ENV import Env
import logging

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)


def create_db_session(db_name: Env.DBName):
    connect_str: str
    if db_name == Env.DBName.MSSQLSERVER:
        connect_str = Env.DBSQLServerEngine
    elif db_name == Env.DBName.MySQL:
        connect_str = Env.DBMySQLEngine
    engine = create_engine(connect_str)
    session = sessionmaker(bind=engine)
    return session
