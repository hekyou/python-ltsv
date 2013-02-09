# -*- encoding: utf-8 -*-

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

def dump(dic, encoding):
    ltsv = u"\t".join(k + u":" + v for k, v in dic.iteritems())
    return ltsv.encode(encoding)

