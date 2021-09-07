import os
import settings
import time

def clear():
    if not settings.verbose:
        os.system('clear')

def print_final_times(times):
    clear()
    print("         SORTING ALGO         |        TIME (s)")
    print("_______________________________________________________")
    for time in times:
        name = time['name']
        total = time['total']
        print("       ", name, ' ' * ( 20 - len(name) ), '|     ', total)

def cool_waiting_gui(name, stop):
    while True:
        clear()
        print('Loading', name, '.')
        if stop(): break
        else: time.sleep(1)
        clear()
        print('Loading', name, '..')
        if stop(): break
        else: time.sleep(1)
        clear()
        print('Loading', name, '...')
        if stop(): break
        else: time.sleep(1)
