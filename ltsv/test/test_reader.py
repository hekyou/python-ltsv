import sys
if sys.version_info[0] == 3:
    from io import StringIO
else:
    from cStringIO import StringIO

from collections import namedtuple
from ltsv import (
        reader,
        DictReader,
        NamedTupleReader,
        )

_testdata = """\
aaa:AAA\tbbb:BBB\tccc:CCC
aaa:AAA1\tbbb:BBB1"""

_expected = [
            [['aaa', 'AAA'], ['bbb', 'BBB'], ['ccc', 'CCC']],
            [['aaa', 'AAA1'], ['bbb', 'BBB1']],
            ]

def pytest_funcarg__file(request):
    return StringIO(_testdata)


def test_reader(file):
    assert list(reader(file)) == _expected

def test_reader_filtered(file):
    rec1, rec2 = reader(file, labels=('ccc',))
    assert rec1 == [['ccc', 'CCC']]
    assert rec2 == []

def test_dictreader(file):
    assert list(DictReader(file)) == list(map(dict, _expected))

def test_namedtuplereader(file):
    nt = namedtuple("testtuple", "aaa ccc")
    rec1, rec2 = NamedTupleReader(file, nt)
    assert rec1.aaa == 'AAA'
    assert rec1.ccc == 'CCC'
    assert rec2.aaa == 'AAA1'
    assert rec2.ccc is None

def test_errors():
    _t = """\
aaa:AAA\tbbb:BBB\tccc:CCC\r
This is broken line.\tAnd next line is empty (valid).
\r
aaa:AAA1\tbbb:BBB1
a#a:AAA
aaa:AAA1\tc#c:CCC\tbbb:BBB1
"""
    records = list(reader(StringIO(_t)))
    assert len(records) == 6
    assert records[0] == _expected[0]
    assert records[1] == []
    assert records[2] == []
    assert records[3] == _expected[1]
    assert records[4] == []
    assert records[5] == _expected[1]

def test_errors_filtered():
    _t = """\
aaa:AAA\tbbb:BBB\tccc:CCC\r
aaa:AAA1\tbbb:BBB1
c#c:CCC
"""
    records = list(reader(StringIO(_t), labels=('bbb','c#c',)))
    assert len(records) == 3
    assert records[0] == [['bbb', 'BBB']]
    assert records[1] == [['bbb', 'BBB1']]
    assert records[2] == []
