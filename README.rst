LTSV parser
===========

Parser implementation in Python

:LTSV:
   | Labeled Tab-separated Values
   | http://ltsv.org/


Installation
------------


Usage
-----

.. code-block:: python

   import ltsv


parsing LTSV string
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   dic = ltsv.reader("ip:127.0.0.1\thost:localhost")
   print dic
   # {u'ip': u'127.0.0.1', u'host': u'localhost'}

   string = ltsv.writer(dic)
   print string
   # ip:127.0.0.1    host:localhost


parsing LTSV file
~~~~~~~~~~~~~~~~~

.. code-block:: python

   lst = ltsv.reader(file("access_log.ltsv"))
   print lst
   # [{u'status': u'200', u'host': u'127.0.0.1', u'req': u'/'}, {u'status': u'200', u'host': u'127.0.0.1', u'req': u'/favicon.ico'}]

   string = ltsv.writer(lst)
   print string
   # status:200      host:127.0.0.1  req:/
   # status:200      host:127.0.0.1  req:/favicon.ico

