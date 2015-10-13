# coding: UTF-8
import random
import re
from optparse import OptionParser

DEFAULT_RANDOM_TYPE = None  # re-define after
DEFAULT_RANDOM_LENGTH = 4
DEFAULT_RANDOM_NUMBER = 1


def get_random_from_format(fo, options):
    for kind in ('int', 'str', 'double'):
        kind_element = '[{}]'.format(kind)
        kind_random_type = {'int': IntRandomType, 'str': StrRandomType,
                            'double': DoubleRandomType}[kind]

        double_pat = r'[+-]?[0-9]*[\.]?[0-9]+'
        kind_element_pat = r'\[{}*({})?(:{})?\]'.format(
            kind, double_pat, double_pat)
        kind_element_match = re.search(kind_element_pat, fo)
        while kind_element_match:
            if kind in ('int', 'double'):
                min_kind = getattr(options, {'int': 'min_int', 'double':
                    'min_double'}[kind])
                max_kind = getattr(options, {'int': 'max_int', 'double':
                    'max_double'}[kind])

            element_min, element_max = kind_element_match.groups()
            if element_min is not None and kind == 'int':
                min_kind = int(element_min)
            elif element_min is not None and kind == 'double':
                min_kind = float(element_min)

            if element_max is not None and kind == 'int':
                element_max = element_max[1:]   # delete ":"
                max_kind = int(element_max)
            elif element_max is not None and kind == 'double':
                element_max = element_max[1:]
                max_kind = float(element_max)
            elif kind == 'str':
                min_kind = max_kind = None

            fo = re.sub(kind_element_pat,
                str(kind_random_type(
                    length=options.length,
                    min_value=min_kind, max_value=max_kind
                ).get_random()),
                    fo,
                    1
                )
            # print(kind_element_match)
            # print(fo, kind_element)
            kind_element_match = re.search(kind_element_pat, fo)
    return fo

class RandomType(object):
    DEFAULT_LENGTH = None

    def __init__(self, length=DEFAULT_RANDOM_LENGTH,
                 min_value=None, max_value=None):
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

    def __eq__(self, other):
        return isinstance(other, self.__class__)


class IntRandomType(RandomType):

    def get_random(self):
        # consider min_value, max_value and length
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


class StrRandomType(RandomType):

    def get_random(self):
        if self.length == 0:
            return ''

        ran = ''
        ran += random.choice(
            'abcdefghiklmnopqrstuvwxyzABCDEFGHIKLMNOPQRSTUVWXYZ_')
        for _ in range(self.length - 1):
            ran += random.choice(
                'abcdefghiklmnopqrstuvwxyzABCDEFGHIKLMNOPQRSTUVWXYZ_123456789')

        return ran


class DoubleRandomType(RandomType):

    def get_random(self):
        """ This method don't see length.
        Use min_double or max_double """
        # consider min_value, max_value and length
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

        t = random.random()
        return (max_value - min_value)*t + min_value

DEFAULT_RANDOM_TYPE = IntRandomType


def get_parser():
    parser = OptionParser()
    parser.add_option(
        '--int',
        action='store_true',
        dest='is_int_random',
        help='occur int random value'
    )
    parser.add_option(
        '--str',
        action='store_true',
        dest='is_str_random',
        help='occur str random value'
    )
    parser.add_option(
        '--double',
        action='store_true',
        dest='is_double_random',
        help='occur double random value'
    )
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
        '--format', '-f',
        type=str,
        dest='fo',
        default=None,
        help='define used format'
    )
    parser.add_option(
        '--min-int',
        type=int,
        dest='min_int',
        default=None,
        help='minimal value of random int values'
    )
    parser.add_option(
        '--min-double',
        type=float,
        dest='min_double',
        default=None,
        help='minimal value of random double values'
    )
    parser.add_option(
        '--max-int',
        type=int,
        dest='max_int',
        default=None,
        help='maximum value of random int values'
    )
    parser.add_option(
        '--max-double',
        type=float,
        dest='max_double',
        default=None,
        help='maximal value of random double values'
    )
    return parser


def get_random_result(options):
    if options.fo:
        return get_random_from_format(options.fo, options)
    else:
        random_type = None
        if options.is_int_random:
            random_type = IntRandomType
        elif options.is_str_random:
            random_type = StrRandomType
        elif options.is_double_random:
            random_type = DoubleRandomType
        else:
            random_type = DEFAULT_RANDOM_TYPE
        min_value = getattr(options, {IntRandomType: 'min_int',
            DoubleRandomType: 'min_double', StrRandomType: 'min_str'}
                [random_type])
        max_value = getattr(options, {IntRandomType: 'max_int',
            DoubleRandomType: 'max_double', StrRandomType: 'max_str'}
                [random_type])
        return random_type(
            length=options.length,
            min_value=min_value, max_value=max_value
        ).get_random()

if __name__ == '__main__':
    (options, args) = get_parser().parse_args()
    if args:
        print('warning: no require argument')
    # print(options)

    random_number = options.number
    random_length = options.length

    for _ in range(random_number):
        ran = get_random_result(options)
        print(ran)
