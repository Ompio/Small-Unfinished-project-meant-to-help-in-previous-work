import test_data
import logging as l
from logging_add_ons import log_variable
# TODO zamienić to na klasę test z wszystkimi metodami oraz zmiennymi/ średni pomysl


def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Podaj poprawną liczbę całkowitą.")


def prepare_test_name(test_name, test):
    test.test_name_list = test_name.split()


def prepare_test_steps_list(number_of_steps, test):
    list_of_steps = []
    for number in range(number_of_steps):
        list_of_steps.append('step_'+str(number)+'_check')
    test.steps = list_of_steps


def prepare_class_name_variations(test):
    test.test_class_name = ''.join(word.title() for word in test.test_name_list)
    test.test_class_name = 'Test' + test.test_class_name
    if test.is_rt:
        test.test_class_name += 'RT'
    else:
        test.test_class_name += 'DT'
    # TODO uzupełnić resztę przypadków, opcja DTRT


def prepare_rt_dt_type(test):
    if str(test.test_name_list[-1]).lower() == 'rt':
        test.is_rt = True
    else:
        test.is_rt = False


def place_by_hand():
    """
    Function filling test data from data inserted by user
    """
    prepare_test_name(input("podaj nazwę twojego testu, skopiowana z tytułu"))
    log_variable(test_data.test_name_list)
    prepare_rt_dt_type(test_data)
    prepare_class_name_variations(test_data)

    number_of_steps = get_integer_input("podaj liczbę kroków w twoim teście")
    log_variable(number_of_steps)
    prepare_test_steps_list(number_of_steps, test_data)
    log_variable(test_data.steps)


def get_from_web():
    """
    Function filling test data from data downloaded from web page
    """
    pass
