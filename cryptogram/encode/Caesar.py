#!/usr/bin/env python
# -*- coding: utf-8 -*-

from string import maketrans
from string import lowercase
from string import uppercase
l = lowercase
u = uppercase


def caesar(s, shift=0):
    '''
    caesar code
    if shift = 0, try every shift here
    '''
    if shift == 0:
        for shift in range(26):
            print trans(s, shift)
    else:
        print trans(s, shift)


def trans(s, t):
    return s.translate(maketrans(l + u, l[t:]+l[:t] + u[t:]+u[:t]))

if __name__ == '__main__':
    s = "oA"
    #s = raw_input()
    caesar(s)
