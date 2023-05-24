import os
import logging


def prepare_inits(test_name):
    logging.debug('active dir: '+os.getcwd())
    with open(r'test_data/__init__.py', 'w') as f:
        pass
    with open(r'scripts/__init__.py', 'w') as f:
        pass
    with open(r'__init__.py', 'w') as f:
        pass


def prepare_dirs(test_name):
    try:
        os.mkdir(test_name)
        logging.debug('udało się utworzyć folder')
    except FileExistsError:
        logging.debug('nie udało się utworzyć folderu z powodu istnienia już folderu o tej samej nazwie')


    os.chdir(test_name)
    try:
        os.mkdir('scripts')
    except FileExistsError:
        logging.debug('nie udało się utworzyć folderu z powodu istnienia już folderu o tej samej nazwie')
    try:
        os.mkdir('test_data')
    except FileExistsError:
        logging.debug('nie udało się utworzyć folderu z powodu istnienia już folderu o tej samej nazwie')

def prepare_files(test_name):
    prepare_dirs(test_name)
    prepare_inits(test_name)
