import os
import sys
import logging
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Base, VersionTable
from sqlalchemy.sql import text
from exception import LoginDbException, SqlSyntaxException, CreateConnectionException


def set_up_logger():
    # set logger
    FORMAT = '[%(levelname)-2s] %(message)s'
    logging.basicConfig(format=FORMAT, level=10)
    logger = logging.getLogger()
    return logger

logger = set_up_logger()

def do_upgrade(db_version, highest_value):
    return highest_value > db_version


def get_scripts(path):
    scripts = os.listdir(path)
    return [file for file in scripts if file.endswith('.sql')]


def get_ordered_scripts(scripts):
    script_dict = {file: get_number_from_filename(file) for file in scripts if get_number_from_filename(file)}
    return sorted(script_dict.keys()), script_dict

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
    try:
        engine = create_engine(db_url)
        Base.metadata.bind = engine
        DBSession = sessionmaker(bind=engine)
        return DBSession()
    except Exception as e:
        logger.error(e)
        raise CreateConnectionException


def run_raw_sql(db_url, statement):
    # it needs error handling
    eng = create_engine(db_url)
    with eng.connect() as con:
        logger.info('Running: {s}'.format(s=statement))
        try:
            rs = con.execute(statement)
        except sqlalchemy.exc.OperationalError as e:
            logger.error(e)
            raise SqlSyntaxException
        

def run_sql_script(db_url, file):
    # it only works with statement in one line
    with open(file, 'r') as f:
        logger.info('running: {}'.format(file))
        for line in f:
            logger.info('running: {}'.format(line))
            try:
                run_raw_sql(db_url, line)
            except SqlSyntaxException as e:
                logger.error(e) 
                sys.exit(3)
            except Exception as e:
                logger.error(e)
                sys.exit(2)
                

def get_db_version(session):
    try:
        version = session.query(VersionTable).first()
    except Exception as e:
        logging.error(e)
        raise LoginDbException
    return int(version.version)


def update_db_version(db_url, new_version):
    session = create_connection(db_url)
    version = session.query(VersionTable).first()
    version.version = new_version
    session.add(version)
    session.commit()
    logger.info('DB version updated: {}'.format(str(version.version)))
    return int(version.version)