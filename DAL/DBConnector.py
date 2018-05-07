from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import logging

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)


engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/test')

db_session = sessionmaker(bind=engine)
