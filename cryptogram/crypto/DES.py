#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint
from DESConstant import *

def genKey():
    return [oddCheck(randint(0, 127)) for i in range(8)]


def oddCheck(x):
    # check a number and make it has odd 1 in bit form
    count = 1
    t = x
    while t:
        t &= t-1
        count ^= 1
    return (x << 1) + count


def repalce(raw, table):
    t = []
    for i in table:
        t.append(raw[i])
    return t

def main():
    # print map(bin,genKey())
    # print repalce(range(64), IP)
    print len(repalce(genKey(), PC1_C))

if __name__ == '__main__':
    main()
