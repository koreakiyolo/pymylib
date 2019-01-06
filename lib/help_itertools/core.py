#!/usr/bin/env python3


from itertools import islice
import collections
from operator import itemgetter
from itertools import groupby

def consume(itertor, n=None):
    if not hasattr(iterator, "__next__"):
        raise TypeError("iterator is invalid type.")
    if n is None:
        collections.deque(itertor, maxlen=0)
    else:
        next(islice(iterator, n, n), None)


def unique_justseen()
