import logging
import os
from menage_files import prepare_files
from read_html_or_place_by_hand import *

if __name__ == '__main__':
    # Make test data from html
    logging.basicConfig(format='\033[97m[\033[92m%(levelname)s\033[97m]-%(message)s', level=logging.DEBUG)
    # prepare_py_files()
    logging.debug('active dir: '+os.getcwd())
    place_by_hand()
    prepare_files()

# TODO naprawić syf związany z singletonem
