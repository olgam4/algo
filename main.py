import sys

from algorithms.time_sort import time_sort
from algorithms.insertion_sort import insertion_sort
from algorithms.pigeonhole_sort import pigeonhole_sort
from algorithms.quick_sort import quick_sort
from algorithms.merge_sort import merge_sort

from helpers.func import *
from helpers.list import *
from helpers.thread import *
from helpers.terminal import *

import settings

def setup_expected_value(list):
    test_list = list.copy()
    test_list.sort()
    return test_list


def setup_argument(length, max_value):
    return create_random_list(length, max_value)


def start_algo(algo_func, algo_name):
    setup_argument_lambda = lambda: setup_argument(settings.array_length, settings.max_value)
    func_def = lambda x: test_func(x, settings.tries, setup_expected_value, setup_argument_lambda)
    stop_threads = False

    algo_thread = ThreadWithReturnValue(target=func_def, args=[algo_func])
    loading_thread = StoppableThread(target=cool_waiting_gui, args=[algo_name, lambda: stop_threads])

    algo_thread.start()
    loading_thread.start()
    return_value = algo_thread.join()
    stop_threads = True
    loading_thread.join()

    return return_value


def main():
    ins_times = start_algo(insertion_sort, 'insertion sort')
    pgh_times = start_algo(pigeonhole_sort, 'pigeonhole sort')
    ts_times = start_algo(time_sort, 'time sort')
    qs_times = start_algo(quick_sort, 'quick sort')
    ms_times = start_algo(merge_sort, 'merge sort')

    times = [
            {"name": "INSERTION SORT", "total": ins_times},
            {"name": "PIGEONHOLE SORT", "total": pgh_times},
            {"name": "TIME SORT", "total": ts_times},
            {"name": "QUICK SORT", "total": qs_times},
            {"name": "MERGE SORT", "total": ms_times}
    ]


    print_final_times(times)


if __name__ == "__main__":
    settings.setup()
    main()
