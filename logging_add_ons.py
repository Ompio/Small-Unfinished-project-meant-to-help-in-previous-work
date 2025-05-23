import logging
import inspect


def log_variable(var):
    # TODO obczić inspect module ale w nowym pliku zeby wszystko nie latało
    caller_frame = inspect.currentframe().f_back
    caller_locals = caller_frame.f_locals
    for name, value in caller_locals.items():
        if value is var:
            logging.debug(f"\033[93m{name}\033[97m: {value}")
            break
