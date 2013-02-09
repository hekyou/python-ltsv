# -*- encoding: utf-8 -*-

def reader(obj, encoding="utf-8"):
    if isinstance(obj, file):
        return self.parse_file(obj, encoding)
    else:
        return self.parse_string(obj, encoding)

def writer(obj, lineterminator="\n", encoding="utf-8"):
    if isinstance(obj, dict):
        return self.dump(obj, encoding)
    elif isinstance(obj, list):
        out = []
        for line in obj:
            out.append(self.dump(line, encoding))
        return lineterminator.join(out)
    else:
        raise ValueError("not support")

def parse_string(string, encoding="utf-8"):
    if isinstance(string, str):
        uni_string = string.decode(encoding).rstrip()
    elif isinstance(string, unicode):
        uni_string = string.rstrip()
    else:
        raise ValueError("not support")
    return dict([x.split(u":", 1) for x in uni_string.split(u"\t")])

def parse_file(handle, encoding="utf-8"):
    return [self.parse_string(line, encoding) for line in handle]

def dump(dic, encoding):
    ltsv = u"\t".join(k + u":" + v for k, v in dic.iteritems())
    return ltsv.encode(encoding)

