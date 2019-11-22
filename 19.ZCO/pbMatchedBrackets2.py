# Code created by Romain Fouilland for problem:
# https://www.codechef.com/ZCOPRAC/problems/ZCO12003

t = int(input())

conversion = ['(', ')', '[', ']']

ints = list(map(lambda c: int(c) - 1, str.split(input(), " ")))


def print_input(ints_list):
    chars = map(lambda c: conversion[c], ints_list)
    print("".join(chars))


def isOpening(c):
    return c % 2 == 0


def getType(c):
    # 0 for () and 1 for []
    return c // 2


def updateLengths(lengths, type):
    lengths[type] += 1
    # but other type increases only if already started
    otherType = 1 - type
    if lengths[otherType] > 0:
        lengths[otherType] += 1


def computeBacth(i0):
    c0 = ints[i0]
    depth = 1
    lengths = [0, 0]
    runningType = getType(c0)
    updateLengths(lengths, runningType)
    di = 1
    c = ints[i0 + di]
    while isOpening(c):
        if runningType != getType(c):
            depth += 1
            runningType = getType(c)
        updateLengths(lengths, runningType)
        di += 1
        c = ints[i0 + di]
    # print_input(ints[i0: i0 + 2 * di])
    return i0 + 2 * di, depth, 2 * lengths[0], 2 * lengths[1]


# print_input(ints)
i = 0
depth = 0
par = 0
bra = 0
while i < len(ints):
    i, batchDepth, batchPar, batchBra = computeBacth(i)
    depth = max(depth, batchDepth)
    par = max(par, batchPar)
    bra = max(bra, batchBra)

print(depth, par, bra)
# Doesn't work on input like ([][]) because of the batch approach
