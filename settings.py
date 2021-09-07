import argparse
from helpers.terminal import clear

def setup():
    global verbose
    global max_value
    global array_length
    global tries

    parser = argparse.ArgumentParser(description="Test the algorithms")

    parser.add_argument("-v", "--verbose", help="Print more info", action='store_true')
    parser.set_defaults(verbose=False)

    args = parser.parse_args()
    verbose = args.verbose

    clear()
    array_length = int(input("Array lengths (50): ") or "50")
    clear()
    max_value = int(input("Max random value (50): ") or "50")
    clear()
    tries = int(input("Tries to find average (5): ") or "5")
    clear()

def setup_test(verbose_value):
    global verbose
    verbose = verbose_value
