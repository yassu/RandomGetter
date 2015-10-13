# coding: UTF-8
import random

DEFAULT_RANDOM_TYPE = int
DEFAULT_RANDOM_FORMAT = '[ran]'
DEFAULT_RANDOM_LENGTH = 4
DEFAULT_RANDOM_NUMBER = 1
DEFAULT_LENGTH_TYPE = 0 # means not absolute

if __name__ == '__main__':
    defalt_random_type = int
    random_number = DEFAULT_RANDOM_NUMBER

    if defalt_random_type == int:
        for _ in range(random_number):
            print(random.randint(-10**(DEFAULT_RANDOM_LENGTH - 1),
                10**(DEFAULT_RANDOM_LENGTH - 1)))
