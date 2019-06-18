#!/usr/bin/python2.7
import os
import sys
import argparse
import utils
import logging
from exception import LoginDbException, SqlSyntaxException, CreateConnectionException

# build parser and parse arguments
parser = argparse.ArgumentParser(description='command line tool to automate db upgrade')

parser.add_argument('path_to_sql', help='path to folder containing sql scripts to use')
parser.add_argument('username', help='db user')
parser.add_argument('host', help='db host')
parser.add_argument('db_name', help='db name')
parser.add_argument('password', help='username db password')
parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0')
parser.add_argument('--debug', action='store_true')
parser.add_argument('--updateVersion')

args = parser.parse_args()

# we can assume the arguments are correct at this point

logger = utils.set_up_logger()


def main():
    
    DB_URL = 'mysql://{user}:{passwd}@{host}/{db}'.format(host=args.host, user=args.username,\
        passwd=args.password,db=args.db_name)
    logger.debug('DB_URL: {url}'.format(url=DB_URL))

    # Error handling for possible sql path location errors.
    try:
        os.path.exists(args.path_to_sql) or os.path.isdir(args.path_to_sql)
    except IOError as e:
        logger.error(e)
        sys.exit(1)

    if args.updateVersion:
        utils.update_db_version(DB_URL, args.updateVersion)
        sys.exit(0)

    # get scripts
    scripts = utils.get_scripts(args.path_to_sql)
    highest_value = utils.get_max_script(scripts)

    try:
        session = utils.create_connection(DB_URL)
    except CreateConnectionException as e:
        logger.error('There was an Error when creating the DB sesion')
        sys.exit(1)
    try:
        version = utils.get_db_version(session)
    except LoginDbException as e:
        logger.error(e)
        sys.exit(4)

    if utils.do_upgrade(version, highest_value):
        # each script which number is higher that version must be executed:
        # lower to higher => version must be updated for each script

        logger.info("Highest value on sql scripts: {max}".format(max=highest_value))
        logger.info("Doing DB upgrade")

        ordered_scripts, scripts_dict = utils.get_ordered_scripts(scripts)
        
        for root, dirs, files in os.walk(args.path_to_sql):
            for f in files:
                if scripts_dict[f] > version:
                    # execute script
                    utils.run_sql_script(DB_URL,  os.path.join(args.path_to_sql, f))
                    # update version
                    version = utils.update_db_version(DB_URL, scripts_dict[f])

        logger.info('Ugrade completed')
        logger.info('New version: {v}'.format(v=version))

    else:
        logger.info('Higher value on sql scripts: {max} is equal or lower than version: {version}'\
                .format(version=version, max=highest_value))
        logger.info('Nothing to do')

if __name__ == '__main__':
    main()
