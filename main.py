#from jinja2 import Template
import logging
import os

from menage_directories import prepare_files


if __name__ == '__main__':
    # Make test data from html
    logging.basicConfig(format='\033[97m[\033[92m%(levelname)s\033[97m]-%(message)s',level=logging.DEBUG)
    prepare_files('nazwa_testu')
    logging.debug('active dir: '+os.getcwd())
