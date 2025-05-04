# The first century spans from the year 1 up to and including the year 100,
# the second century - from the year 101 up to and including the year 200, etc.
#
# Task
# Given a year, return the century it is in.
from math import floor


def century(year: int) -> int:
    century = floor(year / 100)
    if century * 100 < year:
        return century + 1
    else:
        return century