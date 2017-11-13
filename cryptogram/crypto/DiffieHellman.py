#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint

from cryptography import *
from crytest import TESTCASE

def main():
    p = generatePrime(1 << 512, 1 << 514)
    g = primitiveRootRand4Prime(p)

    while True:
        a = randint(1, p-2)
        ga = mrsm(g, a, p)
        if ga != 1:
            break

    while True:
        b = randint(1, p-2)
        gb = mrsm(g, b, p)
        if gb != 1:
            break

    ka = mrsm(gb, a, p)
    kb = mrsm(ga, b, p)

    print 'p:', p
    print 'g:', g
    print 'a:', a
    print 'b:', b    
    print 'ga:', ga
    print 'gb:', gb
    print 'ka:', ka
    print ka == kb

if __name__ == '__main__':
    main()