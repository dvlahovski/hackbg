import math
import sys


def isPrime(num):
    try:
        if num <= 1 or (num % 2 == 0 and num > 2):
            return False
        else:
            return all(num % i for i in xrange(3, int(math.sqrt(num)) + 1, 2))
    except TypeError as e:
        print "isPrime: invalid input, expecting integer"
        print e.message
        return


def primesInAnInterval(start, end):
    if not isinstance(start, (int, long)) or not isinstance(end, (int, long)):
        print "invalid input: start and end should be integers"
        raise TypeError
    if start >= end:
        print "invalid input: start of interval should be smaller than end"
        raise ValueError
    if start < 0 or end < 0:
        print "invalid input: start and end should be positive integers"
        raise ValueError

    try:
        return filter(isPrime, xrange(start, end))
    except:
        print "Unexpected error: ", sys.exc_info()[0]
        raise
