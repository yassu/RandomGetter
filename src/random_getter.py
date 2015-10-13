# coding: UTF-8
import random

DEFAULT_RANDOM_TYPE = int
DEFAULT_RANDOM_LENGTH = 4

if __name__ == '__main__':
    defalt_random_type = int
    if defalt_random_type == int:
        print(random.randint(-10**(DEFAULT_RANDOM_LENGTH - 1),
        10**(DEFAULT_RANDOM_LENGTH - 1)))
