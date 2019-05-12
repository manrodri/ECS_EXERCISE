import os
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Base, VersionTable
from sqlalchemy.sql import text

HOST='localhost'
USERNAME='root'
PASSWORD='password'
DB_NAME='test'
DB_URL = 'mysql://{user}:{passwd}@{host}/{db}'.format(host=HOST, user=USERNAME, passwd=PASSWORD,db=DB_NAME)

def set_up_logger():
    # set logger
    FORMAT = '[%(levelname)-2s] %(message)s'
    logging.basicConfig(format=FORMAT, level=10)
    logger = logging.getLogger()
    return logger

logger= set_up_logger()


def do_upgrade(db_version, highest_value):
    return highest_value > db_version


def get_scripts(path):
    scripts = os.listdir(path)
    return [file for file in scripts if file.endswith('.sql')]


def get_ordered_scripts(scripts):
    script_dict = {file: get_number_from_filename(file) for file in scripts if get_number_from_filename(file)}
    return sorted(script_dict.keys(), reverse=True)


def get_number_from_filename(filename):
    result = []
    for char in filename:
        if char.isdigit():
            result.append(char)
        else:
            break
    number = ''.join(result)
    if number:
        return int(number)


def create_connection(db_url):
    engine = create_engine(db_url)
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    return DBSession()


def run_raw_sql(session, statement):
    # execute statment
    statement = text(statement)
    logger.debug('Executing {raw_sql}'.format(raw_sql=statement))
    result = session.execute(statement)
    logger.info('Success: sql statement run.')
    return result


def get_db_version(session):
    version = session.query(VersionTable).first()
    logger.debug('DB version: {}'.format(version.version))
    return version.version


def update_db_version(db_url, new_version):
    session = create_connection(db_url)
    version = session.query(VersionTable).first()
    version.version = new_version
    session.add(version)
    session.commit()
    logger.info('DB version updated: {}'.format(str(version.version)))