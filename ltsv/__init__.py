# -*- encoding: utf-8 -*-

__version__ = '0.0.5'

from .ltsv import (
        writer,
        dump,
        )

from ._reader import (
        reader,
        DictReader,
        NamedTupleReader,
        )
