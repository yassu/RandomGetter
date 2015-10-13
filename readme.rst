==============
RandomGetter
==============

This project provides a tools for getting various format or kind Random Value 

How to Install
================

::

    $ pip install RandomGetter

or

::

    $ git clone https://github.com/RandomGetter
    $ cd RandomGetter
    $ python install setup.py

Usage
=======

::

    $ random_getter.py [option]

Note that no argument is required.

For example,

::

    $ random_getter.py -f "([double], [str])"
    (-690.8986415091822, _m_c)
    $ random_getter.py -f "([int-10:10], [double:3])"
    (0, -5363.877296867747)
    $ random_getter.py
    -1603

Options
=========

In default, length of random values is 4 and type of random values is `int`.

This means that in default, this program occurs `int` object and -10**4 + 1 <=
random number < 10**4 - 1.

* `--int`: occur `int` random value
* `--str`: occur `str` random value (`str` means ...)
* `--double`: occur `double` random value
* `-n, --number`: indicate number of random values
* `-l, --length`: indicate length of random values
* `--min-int`: indicate minimal value of random int values
* `--max-int`: indicate maximal value of random int values
* `--min-double`: indicate minimal value of random double values
* `--max-double`: indicate maximal value of random double values
* `-f {format}, --format {format}`: indicate format of occured random values

Format
========

::

    $ random_getter.py -f "([int], [double])"
    (568, 5079.63840808)
    $ random_getter.py -f "[int1000]"
    2288
    $ random_getter.py -f "[int:0]"
    -2656
    $ random_getter.py -f "[int-100:100]"
    45

Format is a string which embed "format-element".

"format-element" is one of following style:

* `[{type}]`: random `{type}` value
* `[{type}{min}]`: random `{type}` value more than or equal to `{min}`
* `[{type}:{max}]`: random `{type}` value less than or equal to `{max}`
* `[{type}{min}:{max}]`: random `{type}` value less than or equal to `{max}` and more than or equal to `{min}`

License
=========

Apache License 2.0
