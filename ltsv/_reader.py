# -*- encoding: utf-8 -*-

def reader(ltsvfile, labels=None):
    """Make LTSV Reader for reading selected labels.

    :param  ltsvfile: iterable of lines.
    :param  labels: sequence of labels. (optional)
    :return: generator of record in [[label, value], ...] form.
    """
    if labels is not None:
        prefixes = tuple(L + ':' for L in labels)
        for record in ltsvfile:
            record = record.rstrip('\r\n')
            yield [x.split(':', 1) for x in record.split('\t')
                    if x.startswith(prefixes)]
        return

    for record in ltsvfile:
        record = record.rstrip('\r\n')
        yield [x.split(':', 1) for x in record.split('\t') if x.find(':') > 0]

def DictReader(ltsvfile, labels=None, dict_type=dict):
    """Make LTSV Reader for reading selected labels.

    :param  ltsvfile: iterable of lines.
    :param  labels: sequence of labels.
    :return: generator of record in {label: value, ...} form.
    """
    for rec in reader(ltsvfile, labels):
        yield dict_type(rec)

def NamedTupleReader(ltsvfile, tuple_type):
    arg = (None,) * len(tuple_type._fields)
    default = tuple_type(*arg)
    for rec in reader(ltsvfile, tuple_type._fields):
        yield default._replace(**dict(rec))
