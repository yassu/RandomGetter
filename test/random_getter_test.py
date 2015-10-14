# coding: UTF-8

from random_getter.random_getter import *
import unittest
import re

DEFAULT_OPTIONS, _ = get_parser().parse_args()


def get_random_from_format_test():
    options = DEFAULT_OPTIONS
    options.fo = "[int]"
    res = get_random_from_format(options)
    assert(re.search(r'(-)?\d+', res))
    res = int(res)
    assert(-10**(DEFAULT_RANDOM_LENGTH + 1) <
           res < 10**(DEFAULT_RANDOM_LENGTH + 1))


def get_random_from_format_test2():  # sometimes not passing
    options = DEFAULT_OPTIONS
    options.fo = "[int]"
    options._max = 0
    res = get_random_from_format(options)
    assert(re.search(r'(-)?\d+', res))
    res = int(res)
    assert(res <= 0)


def get_random_from_format_test3():
    options = DEFAULT_OPTIONS
    options.fo = "[int0]"
    res = get_random_from_format(options)
    assert(re.search(r'(-)?\d+', res))
    res = int(res)
    assert(res >= 0)


def get_random_from_format_test4():
    options = DEFAULT_OPTIONS
    options.fo = "[int:100]"
    res = get_random_from_format(options)
    assert(re.search(r'(-)?\d+', res))
    res = int(res)
    assert(res <= 100)


def get_random_from_format_test5():
    options = DEFAULT_OPTIONS
    options.fo = "[int0:100]"
    res = get_random_from_format(options)
    assert(re.search(r'(-)?\d+', res))
    res = int(res)
    assert(0 <= res <= 100)


def get_random_from_format_test6():
    options = DEFAULT_OPTIONS
    options.fo = "[double0]"
    res = get_random_from_format(options)

    assert(re.search(r'[+-]?[0-9]*[\.]?[0-9]+', res))
    res = float(res)
    assert(res >= 0)


def get_random_from_format_test6():
    options = DEFAULT_OPTIONS
    options.fo = "[double:100]"
    res = get_random_from_format(options)

    assert(re.search(r'[+-]?[0-9]*[\.]?[0-9]+', res))
    res = float(res)
    assert(res <= 100)


def get_random_from_format_test7():
    options = DEFAULT_OPTIONS
    options.fo = "[double0:100]"
    res = get_random_from_format(options)

    assert(re.search(r'[+-]?[0-9]*[\.]?[0-9]+', res))
    res = float(res)
    assert(0 <= res <= 100)


class RandomTypeTestCase(unittest.TestCase):

    def length_test(self):
        r = RandomType()
        assert(r.length == DEFAULT_RANDOM_LENGTH)

    def length_test2(self):
        r = RandomType(length=10)
        assert(r.length == 10)

    def min_value_test(self):
        r = RandomType()
        assert(r.min_value is None)

    def min_value_test2(self):
        r = RandomType(min_value=100)
        assert(r.min_value == 100)

    def max_value_test(self):
        r = RandomType()
        assert(r.max_value is None)

    def max_value_test2(self):
        r = RandomType(max_value=100)
        assert(r.max_value == 100)


class IntRandomTestCase(unittest.TestCase):

    def get_random_test(self):
        r = IntRandomType()
        assert(
            -10**(DEFAULT_RANDOM_LENGTH + 1) < r.get_random() <
            10**(DEFAULT_RANDOM_LENGTH + 1))

    def get_random_test2(self):
        r = IntRandomType(min_value=5 * 10**(DEFAULT_RANDOM_LENGTH - 1))
        assert(5 * 10**(DEFAULT_RANDOM_LENGTH - 1) < r.get_random() <
               10**DEFAULT_RANDOM_LENGTH)

    def get_random_test3(self):
        r = IntRandomType(max_value=-5 * 10**(DEFAULT_RANDOM_LENGTH - 1))
        assert(r.get_random() <= -5 * 10**(DEFAULT_RANDOM_LENGTH - 1))


class StrRandomTypeTestCase(unittest.TestCase):

    def get_random_test(self):
        r = StrRandomType()
        assert(len(r.get_random()) == DEFAULT_RANDOM_LENGTH)
        assert(r.get_random()[
               0] in 'abcdefghiklmnopqrstuvwxyzABCDEFGHIKLMNOPQRSTUVWXYZ_')
        assert(r.get_random()[1] in
               'abcdefghiklmnopqrstuvwxyzABCDEFGHIKLMNOPQRSTUVWXYZ_123456789')

    def get_random_test2(self):
        assert(len(StrRandomType(length=100).get_random()) == 100)

    def get_random_test3(self):
        assert(StrRandomType(length=0).get_random() == '')


class DoubleRandomTypeTestCase(unittest.TestCase):

    def get_random_test(self):
        r = DoubleRandomType()
        assert(
            -10**(DEFAULT_RANDOM_LENGTH + 1) < r.get_random() <
            10**(DEFAULT_RANDOM_LENGTH + 1))

    def get_random_test2(self):
        r = DoubleRandomType(max_value=0)
        assert(r.get_random() <= 0)

    def get_random_test3(self):
        r = DoubleRandomType(min_value=0)
        assert(r.get_random() >= 0)


def get_random_type_from_options_test():
    options, _ = get_parser().parse_args()
    options.is_int_random = True
    assert(get_random_type_from_options(options) == IntRandomType)


def get_random_type_from_options_test2():
    options, _ = get_parser().parse_args()
    options.is_str_random = True
    assert(get_random_type_from_options(options) == StrRandomType)


def get_random_type_from_options_test3():
    options, _ = get_parser().parse_args()
    options.is_double_random = True
    assert(get_random_type_from_options(options) == DoubleRandomType)


def get_random_type_from_options_test4():
    options, _ = get_parser().parse_args()
    assert(get_random_type_from_options(options) == DEFAULT_RANDOM_TYPE)


def get_min_value_from_options_test():
    options, _ = get_parser().parse_args()
    assert(get_min_value_from_options(options) is None)


def get_min_value_from_options_test2():
    options, _ = get_parser().parse_args()
    options.min_int = 0
    assert(get_min_value_from_options(options) == 0)


def get_min_value_from_options_test3():
    options, _ = get_parser().parse_args()
    options._min = 0
    assert(get_min_value_from_options(options) == 0)


def get_min_value_from_options_test4():
    options, _ = get_parser().parse_args()
    options.min_int = 0
    options._min = -100
    assert(get_min_value_from_options(options) == -100)


def get_max_value_from_options_test():
    options, _ = get_parser().parse_args()
    assert(get_max_value_from_options(options) is None)


def get_max_value_from_options_test2():
    options, _ = get_parser().parse_args()
    options.max_int = 0
    assert(get_max_value_from_options(options) == 0)


def get_max_value_from_options_test3():
    options, _ = get_parser().parse_args()
    options._max = 0
    assert(get_max_value_from_options(options) == 0)


def get_max_value_from_options_test4():
    options, _ = get_parser().parse_args()
    options.max_int = 0
    options._max = -100
    assert(get_max_value_from_options(options) == -100)
