#!/usr/bin/python2.7

import argparse
import utils

HOST='localhost'
USERNAME='root'
PASSWORD='password'
DB_NAME='test'
DB_URL = 'mysql://{user}:{passwd}@{host}/{db}'.format(host=HOST, user=USERNAME, passwd=PASSWORD,db=DB_NAME)

logger = utils.set_up_logger()

# build parser and parse arguments
parser = argparse.ArgumentParser(description='command line tool to automate db upgrade')

parser.add_argument('path_to_sql', help='path to folder containing sql scripts to use')
parser.add_argument('username', help='db user')
parser.add_argument('host', help='db host')
parser.add_argument('db_name', help='db name')
parser.add_argument('password', help='username db password')
parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0')

args = parser.parse_args()

# we can assume the arguments are correct at this point

def main():
    # get scripts
    scripts = utils.get_scripts(args.path_to_sql)
    highest_value = utils.get_max_script(scripts)

    session = utils.create_connection(DB_URL)
    version = utils.get_db_version(session)
    #ordered_scripts = utils.get_ordered_scripts(scripts)


    if utils.do_upgrade(version, highest_value):

        logger.info("Highest value on sql scripts: {max}".format(max=highest_value))
        logger.info("Doing DB upgrade")

        ordered_scripts, scripts_dict = utils.get_ordered_scripts(scripts)
        for script in ordered_scripts:
            if scripts_dict[script] > version:
                # execute script
                utils.run_sql_script(DB_URL, script)
                # update version
                version = utils.update_db_version(DB_URL, scripts_dict[script])

        logger.info('Ugrade completed')
        logger.info('New version: {v}'.format(v=version))


if __name__ == '__main__':
    main()