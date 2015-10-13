# coding: UTF-8
from setuptools import setup
from random_getter.random_getter import __VERSION__

setup(
    name='RandomGetter',
    version=__VERSION__,
    author='yassu',
    author_email="mathyassu@gmail.com",

    packages=['random_getter'],
    description=('This project provides a tools for getting various format '
        'or kind Random Value.'),
    long_description=open("readme.rst").read(),
    url= 'https://github.com/yassu/RandomGetter',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'License :: Freeware',
        'License :: OSI Approved :: Apache Software License',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    license=(
        'Released Under the Apache license\n'
        'https://github.com/yassu/RandomGetter\n'
    ),
    scripts=['random_getter/random_getter.py']
)
