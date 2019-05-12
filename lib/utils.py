import os
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Base, VersionTable
from sqlalchemy.sql import text



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
    return sorted(script_dict.keys(), reverse=True), script_dict

def get_max_script(scripts):
    return max([get_number_from_filename(file) for file in scripts if get_number_from_filename(file)])


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


def run_raw_sql(db_url, statement):
    # it needs error handling
    eng = create_engine(db_url)
    with eng.connect() as con:
        rs = con.execute(statement)
        data = rs.fetchone()[0]
        logger.info("Data: %s" % data)

def run_sql_script(db_url, file):
    for line in file:
        try:
            run_raw_sql(db_url, line)
        except Exception:
            pass

def get_db_version(session):
    version = session.query(VersionTable).first()
    logger.debug('DB version: {}'.format(version.version))
    return int(version.version)


def update_db_version(db_url, new_version):
    session = create_connection(db_url)
    version = session.query(VersionTable).first()
    version.version = new_version
    session.add(version)
    session.commit()
    logger.info('DB version updated: {}'.format(str(version.version)))