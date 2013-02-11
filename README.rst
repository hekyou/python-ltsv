LTSV parser
===========

.. image:: https://travis-ci.org/hekyou/python-ltsv.png?branch=master
   :target: https://travis-ci.org/hekyou/python-ltsv

Parser implementation in Python

:LTSV:
   | Labeled Tab-separated Values
   | http://ltsv.org/


Installation
------------

::

    pip install ltsv

Usage
-----

parsing
~~~~~~~

csv like interface::

    >>> import sys
    >>> if sys.version_info[0] == 3:
    ...     from io import StringIO
    ... else:
    ...     from cStringIO import StringIO
    ...
    >>> import ltsv
    >>> reader = ltsv.reader(StringIO("ip:127.0.0.1\thost:localhost"))
    >>> next(reader)
    [['ip', '127.0.0.1'], ['host', 'localhost']]

writing
~~~~~~~~

::

   dic = {u'ip': u'127.0.0.1', u'host': u'localhost'}
   string = ltsv.writer(dic)
   print(string)
   # ip:127.0.0.1    host:localhost
