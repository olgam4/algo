import time

from helpers.math import average

import settings

def time_this(func):
    start_time = time.time()
    return_value = func()
    total_time = time.time() - start_time
    return return_value, total_time

def test_func(func, tries, setup_expected_value, setup_argument):
    times = []
    for _ in range(tries):
        func_argument = setup_argument()
        expected_value = setup_expected_value(func_argument)

        return_value, total_time = time_this(lambda: func(func_argument))

        if settings.verbose:
            print(func, "returned", return_value)

        times.append(total_time)

        if return_value != expected_value:
            print(func, "failed")
            break

    return average(times)

