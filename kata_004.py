# You will be given an array a and a value x. All you need to do is check whether the provided array contains the value.
#
# a can contain numbers or strings. x can be either.
#
# Return true if the array contains the value, false if not.
from array import *


def check(seq: array|list, elem: any) -> bool:
    if isinstance(seq, array):
        return seq.tolist().count(elem) > 0
    else:
        return seq.count(elem) > 0