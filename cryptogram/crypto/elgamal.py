#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint

from cryptography import *
from crytest import TESTCASE


class ElGamal(object):

    """
    a simple project for ElGamal
    """

    def __init__(self, a=1 << 512, b=1 << 514):
        '''
        gen key for elgamal
        public key: (p,g,y)
        private key: x
        '''
        self.p = generatePrime(a, b)
        self.g = primitiveRootRand4Prime(self.p)

        while True:
            self.x = randint(1, self.p-2)
            self.y = mrsm(self.g, self.x, self.p)
            if self.y != 1:
                break

    def encrypt(self, m):
        while True:
            k = randint(1, self.p-2)
            c1 = mrsm(self.g, k, self.p)
            if c1 != 1:
                break
        c2 = (mrsm(self.y, k, self.p) * msg2num(m)) % self.p
        return c1, c2,

    def decrypt(self, c1, c2):
        return num2msg((c2*inverse(mrsm(c1, self.x, self.p), self.p)) % self.p)


# __DEBUG = True
__DEBUG = False


def main():

    if __DEBUG:
        plain = raw_input('your plain: ')
    else:
        plain = TESTCASE[:60]

    e = ElGamal()

    cryptograph = e.encrypt(plain)
    re = e.decrypt(cryptograph[0], cryptograph[1])

    print 'plain: ', plain
    print 'cry: ', cryptograph

    if plain == re:
        print "You did it!"

if __name__ == '__main__':
    main()
