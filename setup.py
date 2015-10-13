# coding: UTF-8
from setuptools import setup

setup(
    name='RandomGetter',
    version='0.0.1',
    packages=['random_getter'],
    description=('This project provides a tools for getting various format or'
        'kind.'),
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
    author_email="mathyassu@gmail.com",
    license=(
        'Released Under the Apache license\n'
        'https://github.com/yassu/RandomGetter\n'
    ),
    scripts=['random_getter/random_getter.py']

)
