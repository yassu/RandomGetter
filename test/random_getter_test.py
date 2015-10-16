# coding: UTF-8

from random_getter.random_getter import *
from nose.tools import raises
import unittest
import re

RANDOM_TEST_NUMBER = 10


def get_default_option():
    options, _ = get_parser().parse_args()
    return options


def get_random_from_format_test():
    options = get_default_option()
    options.fo = "[int]"
    for _ in range(RANDOM_TEST_NUMBER):
        res = get_random_from_format(options)
        assert(re.search(r'(-)?\d+', res))
        res = int(res)
        assert(-10**(DEFAULT_RANDOM_LENGTH + 1) <
               res < 10**(DEFAULT_RANDOM_LENGTH + 1))


def get_random_from_format_test2():  # sometimes not passing
    options = get_default_option()
    for _ in range(RANDOM_TEST_NUMBER):
        options.fo = "[int]"
        options._max = 0
        res = get_random_from_format(options)
        assert(re.search(r'(-)?\d+', res))
        res = int(res)
        assert(res <= 0)


def get_random_from_format_test3():
    options = get_default_option()
    options.fo = "[int0]"
    for _ in range(RANDOM_TEST_NUMBER):
        res = get_random_from_format(options)
        assert(re.search(r'(-)?\d+', res))
        res = int(res)
        assert(res >= 0)


def get_random_from_format_test4():
    options = get_default_option()
    options.fo = "[int:100]"
    for _ in range(RANDOM_TEST_NUMBER):
        res = get_random_from_format(options)
        assert(re.search(r'(-)?\d+', res))
        res = int(res)
        assert(res <= 100)


def get_random_from_format_test5():
    options = get_default_option()
    options.fo = "[int0:100]"
    for _ in range(RANDOM_TEST_NUMBER):
        res = get_random_from_format(options)
        assert(re.search(r'(-)?\d+', res))
        res = int(res)
        assert(0 <= res <= 100)


def get_random_from_format_test6():
    options = get_default_option()
    options.fo = "[double0]"
    for _ in range(RANDOM_TEST_NUMBER):
        res = get_random_from_format(options)

        assert(re.search(r'[+-]?[0-9]*[\.]?[0-9]+', res))
        res = float(res)
        assert(res >= 0)


def get_random_from_format_test6():
    options = get_default_option()
    options.fo = "[double:100]"
    for _ in range(RANDOM_TEST_NUMBER):
        res = get_random_from_format(options)

        assert(re.search(r'[+-]?[0-9]*[\.]?[0-9]+', res))
        res = float(res)
        assert(res <= 100)


def get_random_from_format_test7():
    options = get_default_option()
    options.fo = "[double0:100]"
    for _ in range(RANDOM_TEST_NUMBER):
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
        for _ in range(RANDOM_TEST_NUMBER):
            assert(
                -10**(DEFAULT_RANDOM_LENGTH + 1) < r.get_random() <
                10**(DEFAULT_RANDOM_LENGTH + 1))

    def get_random_test2(self):
        r = IntRandomType(min_value=5 * 10**(DEFAULT_RANDOM_LENGTH - 1))
        for _ in range(RANDOM_TEST_NUMBER):
            assert(5 * 10**(DEFAULT_RANDOM_LENGTH - 1) < r.get_random() <
                   10**DEFAULT_RANDOM_LENGTH)

    def get_random_test3(self):
        r = IntRandomType(max_value=-5 * 10**(DEFAULT_RANDOM_LENGTH - 1))
        for _ in range(RANDOM_TEST_NUMBER):
            assert(r.get_random() <= -5 * 10**(DEFAULT_RANDOM_LENGTH - 1))


class StrRandomTypeTestCase(unittest.TestCase):

    def get_random_test(self):
        r = StrRandomType()
        for _ in range(RANDOM_TEST_NUMBER):
            assert(len(r.get_random()) == DEFAULT_RANDOM_LENGTH)
            assert(r.get_random()[0]
                   in 'abcdefghiklmnopqrstuvwxyzABCDEFGHIKLMNOPQRSTUVWXYZ_')
            assert(r.get_random()[1] in
                   'abcdefghiklmnopqrstuvwxyzABCDEFGHIKLMNOPQRSTUVWXYZ_'
                   '123456789')

    def get_random_test2(self):
        for _ in range(RANDOM_TEST_NUMBER):
            assert(len(StrRandomType(length=100).get_random()) == 100)

    def get_random_test3(self):
        for _ in range(RANDOM_TEST_NUMBER):
            assert(StrRandomType(length=0).get_random() == '')


class DoubleRandomTypeTestCase(unittest.TestCase):

    def get_random_test(self):
        r = DoubleRandomType()
        for _ in range(RANDOM_TEST_NUMBER):
            assert(
                -10**(DEFAULT_RANDOM_LENGTH + 1) < r.get_random() <
                10**(DEFAULT_RANDOM_LENGTH + 1))

    def get_random_test2(self):
        r = DoubleRandomType(max_value=0)
        for _ in range(RANDOM_TEST_NUMBER):
            assert(r.get_random() <= 0)

    def get_random_test3(self):
        r = DoubleRandomType(min_value=0)
        for _ in range(RANDOM_TEST_NUMBER):
            assert(r.get_random() >= 0)


def get_random_type_from_options_test():
    options = get_default_option()
    options.is_int_random = True
    assert(get_random_type_from_options(options) == IntRandomType)


def get_random_type_from_options_test2():
    options = get_default_option()
    options.is_str_random = True
    assert(get_random_type_from_options(options) == StrRandomType)


def get_random_type_from_options_test3():
    options = get_default_option()
    options.is_double_random = True
    assert(get_random_type_from_options(options) == DoubleRandomType)


def get_random_type_from_options_test4():
    options = get_default_option()
    assert(get_random_type_from_options(options) == DEFAULT_RANDOM_TYPE)


def get_min_value_from_options_test():
    options = get_default_option()
    assert(get_min_value_from_options(options) is None)


def get_min_value_from_options_test2():
    options = get_default_option()
    options.min_int = 0
    assert(get_min_value_from_options(options) == 0)


def get_min_value_from_options_test3():
    options = get_default_option()
    options._min = 0
    assert(get_min_value_from_options(options) == 0)


def get_min_value_from_options_test4():
    options = get_default_option()
    options._min = -100
    options.min_int = 0  # more priority
    assert(get_min_value_from_options(options) == 0)


def get_max_value_from_options_test():
    options = get_default_option()
    assert(get_max_value_from_options(options) is None)


def get_max_value_from_options_test2():
    options = get_default_option()
    options.max_int = 0
    res = get_max_value_from_options(options)
    assert(res == 0)


def get_max_value_from_options_test3():
    options = get_default_option()
    options._max = 0
    assert(get_max_value_from_options(options) == 0)


def get_max_value_from_options_test4():
    options = get_default_option()
    options.max_int = 0  # more priority
    options._max = -100
    assert(get_max_value_from_options(options) == 0)


def get_random_result_test5():
    # for str case 1
    options = get_default_option()
    options.is_str_random = True
    res = get_random_result(options)
    assert(res[0] in 'abcdefghiklmnopqrstuvwxyzABCDEFGHIKLMNOPQRSTUVWXYZ_')
    assert(res[1] in
           'abcdefghiklmnopqrstuvwxyzABCDEFGHIKLMNOPQRSTUVWXYZ_123456789')


def get_random_result_test6():
    # for str case 2
    options = get_default_option()
    options.is_str_random = True
    options.length = 6
    res = get_random_result(options)
    assert(len(res) == 6)

def check_option_test():
    options = get_default_option()
    check_option(options)   # don't raise Exception

def check_option_test2():
    options = get_default_option()
    options.is_double = True
    check_option(options)   # don't raise Exception

@raises(IllegalOptionMatchException)
def check_option_test3():
    options = get_default_option()
    options.is_double_random = True
    options.is_str_random = True
    check_option(options)   # raise Exception

@raises(IllegalOptionMatchException)
def check_option_test4():
    options = get_default_option()
    options.is_int_random = True
    options.is_double_random = True
    options.is_str_random = True
    check_option(options)
