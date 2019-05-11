import os
import logging
import re

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

def get_number_from_filename(filename):
    # 1 char is a number: store it
    # 1 char is not an number then error -> exclude file from executing
    # 2 char is a number append it -> continue
    # 2 is not number -> return number
    # 3 char is number append it -> continue
    # 3 is not number -> return number ...
    pass

def get_ordered_scripts(scripts):
    # order the scripts according the following criteria:
    # order from top to bottom.
    # file name not always contain a dot separating number from name.
    # each file name contain a number part and a name part despite numbers can be part of the name.
    # number part are not correlative.
    # regex that matches our filenames: \d+\.?[a-zA-Z]+
    pass