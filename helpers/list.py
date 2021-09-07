import random

def create_random_list(len_list, max_value):
    list = []
    for i in range(1, len_list + 1):
        list.append(random.randint(0, max_value))
    return list

