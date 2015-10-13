# coding: UTF-8

from sys import path
path.append('src')
from random_getter import *

from unittest import TestCase


class RandomTypeTestCase(TestCase):

    def length_test(self):
        r = RandomType()
        print(r.length)
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


class IntRandomTestCase(TestCase):

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


class StrRandomTypeTestCase(TestCase):

    def get_random_test(self):
        r = StrRandomType()
        assert(len(r.get_random()) == DEFAULT_RANDOM_LENGTH)
        assert(r.get_random()[
               0] in 'abcdefghiklmnopqrstuvwxyzABCDEFGHIKLMNOPQRSTUVWXYZ_')
        assert(r.get_random()[1] in
               'abcdefghiklmnopqrstuvwxyzABCDEFGHIKLMNOPQRSTUVWXYZ_123456789')

    def get_random_test2(self):
        assert(len(StrRandomType(length=100).get_random()) == 100)
