import threading
import time
from algorithms.insertion_sort import insertion_sort

def sort_function(value, final_array):
    sleeping_time = value / 1000
    time.sleep(sleeping_time)
    final_array.append(value)

def time_sort(list):
    threads, final_array = [], []
    for j in list:
        u = threading.Thread(target=sort_function, args=[j, final_array])
        u.start()
        threads.append(u)
    for k in threads:
        k.join()
    final_array = insertion_sort(final_array)
    return final_array
