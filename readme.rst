==============
RandomGetter
==============

This project provides a tools for getting various format or kind 

How to Install
================

::

    $ python install setup.py

Usage
=======

::

    $ random_getter.py [option]

Note that no argument is required.

For example,

::

    $ random_getter.py -f "([double], [str])"
    ran: (-690.8986415091822, _m_c)
    $ random_getter.py -f "([int-10:10], [double:3])"
    ran: (0, -5363.877296867747)
    $ random_getter.py
    ran: -1603

License
=========

Apache License 2.0