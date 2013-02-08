from ltsv import Ltsv
ltsv = Ltsv()

class TestParseString:
    def test_one_param(self):
        assert ltsv.parse_string("ip:127.0.0.1") == {u"ip": u"127.0.0.1"}

    def test_several_param(self):
        assert ltsv.parse_string("ip:127.0.0.1\thost:localhost") \
                == {u"ip": u"127.0.0.1", u"host": u"localhost"}

    def test_double_colon(self):
        assert ltsv.parse_string("host:local:host") \
                == {u"host": u"local:host"}

