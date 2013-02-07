# -*- encoding: utf-8 -*-

class Ltsv(object):
    def __init__(self):
        pass

    def reader(self, obj, encoding="utf-8"):
        if isinstance(obj, file):
            return self.parse_file(obj, encoding)
        else:
            return self.parse_string(obj, encoding)

    def writer(self, obj, lineterminator="\n", encoding="utf-8"):
        if isinstance(obj, dict):
            return self.dump(obj, encoding)
        elif isinstance(obj, list):
            out = []
            for line in obj:
                out.append(self.dump(line, encoding))
            return lineterminator.join(out)
        else:
            raise ValueError("not support")

    def parse_string(self, string, encoding):
        if isinstance(string, str):
            uni_string = string.decode(encoding).rstrip()
        elif isinstance(obj, unicode):
            uni_string = string.rstrip()
        else:
            raise ValueError("not support")
        return dict([x.split(u":") for x in uni_string.split(u"\t")])

    def parse_file(self, handle, encoding):
        out = []
        for line in handle:
            out.append(self.parse_string(line, encoding))
        return out

    def dump(self, dic, encoding):
        ltsv = u"\t".join(k + u":" + v for k, v in dic.iteritems())
        return ltsv.encode(encoding)

