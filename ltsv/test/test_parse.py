from ltsv import *

def test_one_param():
    assert parse_string("ip:127.0.0.1") == {u"ip": u"127.0.0.1"}

def test_several_param():
    assert parse_string("ip:127.0.0.1\thost:localhost") \
            == {u"ip": u"127.0.0.1", u"host": u"localhost"}

def test_double_colon():
    assert parse_string("host:local:host") == {u"host": u"local:host"}

