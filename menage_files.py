import os
import logging
from jinja2 import Template
import test_data as test


def prepare_inits(test_name):
    logging.debug('active dir: ' + os.getcwd())
    with open(r'test_data/__init__.py', 'w') as f:
        pass
    with open(r'scripts/__init__.py', 'w') as f:
        pass
    with open(r'__init__.py', 'w') as f:
        pass


def prepare_dirs():
    try:
        os.mkdir(test.test_name_snake_case)
        logging.debug('udało się utworzyć folder')
    except FileExistsError:
        logging.debug('nie udało się utworzyć folderu z powodu istnienia już folderu o tej samej nazwie')

    os.chdir(test.test_name_snake_case)
    try:
        os.mkdir('scripts')
    except FileExistsError:
        logging.debug('nie udało się utworzyć folderu z powodu istnienia już folderu o tej samej nazwie')
    try:
        os.mkdir('test_data')
    except FileExistsError:
        logging.debug('nie udało się utworzyć folderu z powodu istnienia już folderu o tej samej nazwie')


def prep_steps():
    template = Template('''
# -*- coding: utf-8 -*-
"""
Module containing UserWidgetAliasesRTSteps class
"""
# TODO poprawić docstring
from engine.verification.verify import verify_condition
from shared.base_classes.base_steps import BaseSteps
# TODO poprawnie ponazywać importy
from testsuites.opc_ua.advanced.offline_import_to_client_an_xml_companion_spec_dt.scripts.config import (
    UserWidgetAliasesRTConfig,
)
from testsuites.opc_ua.advanced.offline_import_to_client_an_xml_companion_spec_dt.test_data.expected_values import (
    BaseValues,
    ValuesForStep,
    MotorInstances,
)

# TODO zmienić nazwę na odpowiednią
class {test.name}(BaseSteps):
    """
    Test steps for {test.name}
    """
    # TODO zmienić docstring
    config: {test.config}
    # TODO zmienić configa razem z importem
    # TODO automatyczne tworzenie stepów
    {% for step in steps %}
        def {step}(self) -> None:
            """Check that all controls values are good in the runtime"""
            # TODO zmienić docstring
    {% endfor %}
    # przykład użycia verify_condition
    verify_condition(
        self.config.motorwidget1_acceleration.get_value,
        BaseValues.MOTOR_WIDGET_1.ACCELERATION,
        f"Verify that MotorWidget1 acceleration value is equal to {BaseValues.MOTOR_WIDGET_1.ACCELERATION}",
    )
    ''')
    print(template.render(steps=test.steps))  # , test=test.test_data)) TODO potrzebne?
    pass


def prep_config():
    pass


def prep_remote_projects():
    pass


def prep_classes_with_data():
    # TODO zrobić klasy z informacjami
    pass


def prep_test():
    pass


def prepare_py_files():
    prep_steps()
    prep_config()
    prep_remote_projects()
    prep_classes_with_data()
    prep_test()


def prepare_files():
    prepare_dirs()
    prepare_inits()
    prepare_py_files()
