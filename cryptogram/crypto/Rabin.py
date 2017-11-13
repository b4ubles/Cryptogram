#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cryptography import *
from crytest import TESTCASE


class Rabin():

    """
    a simple calss which use to encrypt and decrypt by Rabin
    public key: b, n
    private key: p, q
    """

    STRLEN = 100

    def __init__(self):
        pass
        #super(Rabin, self).__init__()
        #self.arg = arg

    @staticmethod
    def genkey(a, b):
        while True:
            # print "try p \t"
            p = randint(a, b)
            if p % 4 != 3:
                continue
            if MillerRabin(p):
                break

        while True:
            # print "try p \t"
            q = randint(a, b)
            if q % 4 != 3 or q == p:
                continue
            if MillerRabin(q):
                break

        return p, q

    @staticmethod
    def encrypt(m, n):
        return ((msg2num(m)*Rabin.STRLEN)**2) % n

    @staticmethod
    def decrypt(i, p, q):
        re = Rabin.sqrt(i, p, q)
        for i in re:
            if i % Rabin.STRLEN == 0:
                return num2msg(i/Rabin.STRLEN)
                # plaintext.append(j)

    @staticmethod
    def sqrt(c, p, q):
        x = squareRootModp4(c, p)
        y = squareRootModp4(c, q)
        s, t = Euclidean(q, p)

        '''
        if s*q + q*t == 1:
            print "True"
        else:
            print "False"
        '''

        n = p*q
        re = []
        re.append((x*s*q+y*t*p) % (n))
        re.append((x*s*q-y*t*p) % (n))
        re.append((-x*s*q+y*t*p) % (n))
        re.append((-x*s*q-y*t*p) % (n))
        return re

__DEBUG = True
# __DEBUG = False


def main():

    p, q = Rabin.genkey(1 << 512, 1 << 514)
    n = p*q
    # public key : n
    # private key : (p, q)

    if p % 4 != 3 or q % 4 != 3:
        print "error!"
        return

    if __DEBUG:
        msg = TESTCASE
    else:
        msg = raw_input()

    msg_list = []

    i = 0
    LEN = 100
    while True:
        if i < len(msg)-LEN:
            msg_list.append(msg[i:i+LEN])
            i += LEN
        else:
            msg_list.append(msg[i:])
            break

    cryptograph = []

    # encryption
    for m in msg_list:
        cryptograph.append(Rabin.encrypt(m, n))

    plaintext = []

    # decryption
    for i in cryptograph:
        plaintext.append(Rabin.decrypt(i, p, q))

    re = ''
    for m in plaintext:
        re += str(m)

    if __DEBUG:
        print msg_list
        print cryptograph
        print "plain", plaintext
        print re

    if msg == re:
        print "You did it!"

if __name__ == '__main__':
    main()
