# coding: UTF-8
import random
from optparse import OptionParser

DEFAULT_RANDOM_TYPE = int
DEFAULT_RANDOM_FORMAT = '[ran]'
DEFAULT_RANDOM_LENGTH = 4
DEFAULT_RANDOM_NUMBER = 1
DEFAULT_LENGTH_TYPE = 0 # means not absolute

class RandomType(object):
    DEFAULT_LENGTH = None

    def __init__(self, length=DEFAULT_RANDOM_LENGTH, min_value=None, max_value=None):
        self._length = length
        self._min_value = min_value
        self._max_value = max_value

    @property
    def length(self):
        return self._length

    @property
    def min_value(self):
        return self._min_value

    @property
    def max_value(self):
        return self._max_value

    def get_random(self):
        pass

class IntRandomType(RandomType):
    DEFAULT_LENGTH = 4

    def __init__(self, length=DEFAULT_RANDOM_LENGTH, min_value=None,
            max_value=None):
        RandomType.__init__(self, length=length, min_value=min_value,
        max_value=max_value)

    def get_random(self):
        # consider min_value, max_value and length
        # (TODO: case absolute length type)
        if self.min_value is None:
            min_value = -(10**self.length - 1)
        else:
            min_value = self.min_value
        # TODO: if min_value < -10**(self.length + 1), raise error

        if self.max_value is None:
            max_value = 10**self.length - 1
        else:
            max_value = self.max_value
        # TODO: if max_value > 10** (self.length + 1), lraise error

        return random.randint(min_value, max_value)

def get_parser():
    parser = OptionParser()
    parser.add_option(
        '--number', '-n',
        type=int,
        dest='number',
        default=DEFAULT_RANDOM_NUMBER,
        help='number of random results'
    )
    parser.add_option(
        '--length', '-l',
        type=int,
        dest='length',
        default=DEFAULT_RANDOM_LENGTH,
        help='length of random values(int, double or str)'
    )
    parser.add_option(
        '--min-int',
        type=int,
        dest='min_int',
        default=None,
        help='minimal value of random int values'
    )
    parser.add_option(
        '--max-int',
        type=int,
        dest='max_int',
        default=None,
        help='maximum value of random int values'
    )
    return parser

if __name__ == '__main__':
    (options, _) = get_parser().parse_args()
    print(options)

    defalt_random_type = int
    random_number = options.number
    random_length = options.length

    if defalt_random_type == int:
        for _ in range(random_number):
            ran = IntRandomType(
                length=options.length,
                min_value=options.min_int, max_value=options.max_int
                ).get_random()
            print(ran)
