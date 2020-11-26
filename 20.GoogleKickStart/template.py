# -- coding: utf-8 --
import bisect
import heapq
import math

import random
import sys
from collections import Counter, defaultdict, deque

from decimal import ROUND_CEILING, ROUND_HALF_UP, Decimal
from functools import lru_cache, reduce
from itertools import combinations, combinations_with_replacement, product, permutations, starmap
from operator import add, mul, ne, pos, sub
from fractions import Fraction

sys.setrecursionlimit(100000)


def read_int():
    return int(input())


def read_int_n():
    return list(map(int, input().split()))


def read_float():
    return float(input())


def read_float_n():
    return list(map(float, input().split()))


def read_str():
    return input().strip()


def read_str_n():
    return list(map(str, input().split()))


def error_print(*args):
    print(*args, file=sys.stderr)


def mt(f):
    import time

    def wrap(*args, **kwargs):
        s = time.time()
        ret = f(*args, **kwargs)
        e = time.time()

        error_print(e - s, 'sec')
        return ret

    return wrap


def gcd(x, y):
    if x < y:
        return gcd(y, x)
    if y == 0:
        return x
    return gcd(y, x % y)


def printinput(func):
    def wrap(*args):
        print(args)
        return func(*args)

    return wrap


def printio(func):
    def wrap(*args):
        res = func(*args)
        print(func.__name__, args, res)
        return res

    return wrap


def multip(elts):
    res = 1
    for elt in elts:
        res *= elt
    return res


def solve(str_):
    nb_kicks = 0
    result = 0
    for i in range(len(str_) - 4):
        if str_[i : i + 4] == 'KICK':
            nb_kicks += 1
        elif str_[i : i + 5] == 'START':
            result += nb_kicks
    return result


def main():
    T = read_int()
    for test_number in range(T):
        str_ = read_str()
        ans = solve(str_)
        print("Case #{}: {}".format(test_number + 1, ans))


if __name__ == '__main__':
    main()
