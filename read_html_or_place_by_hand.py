import test_data as test
from logging_add_ons import log_variable


def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Podaj poprawną liczbę całkowitą.")


def prepare_test_name(test_name):
    test.test_name_list = test_name.split()


def prepare_test_steps_list(number_of_steps):
    list_of_steps = []
    for number in range(number_of_steps):
        list_of_steps.append('step_'+str(number)+'_check')
    test.steps = list_of_steps


def prepare_class_name_variations():
    test.test_class_name = ''.join(word.title() for word in test.test_name_list)
    test.test_class_name = 'Test' + test.test_class_name
    # TODO nazwa testu + test variation o ile to ma sens bo jest to ostatnia część z logiki

def prepare_rt_dt_type():
    if str(test.test_name_list[-1]).lower() == 'rt':
        test.test_type = True
    else:
        test.test_type = False


def place_by_hand():
    """
    Function filling test data from data inserted by user
    """
    prepare_test_name(input("podaj nazwę twojego testu, skopiowana z tytułu"))
    prepare_rt_dt_type()
    prepare_class_name_variations()

    number_of_steps = get_integer_input("podaj liczbę kroków w twoim teście")
    prepare_test_steps_list(number_of_steps)


def get_from_web():
    """
    Function filling test data from data downloaded from web page
    """
    pass
