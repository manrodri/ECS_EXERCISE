#!/usr/bin/python2.7

import logging
import argparse
import utils
#import mysql.connector
#from mysql.connector import Error

logger = utils.set_up_logger()

# build parser and parse arguments
parser = argparse.ArgumentParser(description='command line tool to automate db upgrade')

parser.add_argument('directory-with-sql-scripts', help='path to folder containing sql scripts to use')
parser.add_argument('username', help='db user')
parser.add_argument('host', help='db host')
parser.add_argument('db-name', help='db name')
parser.add_argument('password', help='username db password')
parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0')

args = parser.parse_args()

# we can assume the arguments are correct at this point

def main():
    print args

if __name__ == '__main__':
    main()