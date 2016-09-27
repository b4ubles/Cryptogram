from cryptography import *
from unit_test import TESTCASE

class RSA():

    """
    a simple calss which use to encrypt and decrypt by RSA
    """

    def __init__(self):
        pass

    def genkey(self, a, b):
        p = generatePrime(a, b)
        q = generatePrime(a, b)
        while q == p:
            q = generatePrime(a, b)

        n = p*q
        phi = (p-1)*(q-1)
        e = self.gete(phi)
        d = Euclidean(e, phi)[0] % phi

        return e, d, n

    def gete(self, phi):
        while True:
            e = randint(2, phi-1)
            if gcd(e, phi) == 1:
                break
        return e

    def getd(self, p, q, e):
        phi = (p-1)*(q-1)
        d = Euclidean(e, phi)[0] % phi

        return d

    def encrypt(self, m, e, n):
        num = msg2num(m)
        return mrsm(num, e, n)

    def decrypt(self, c, d, n):
        return num2msg(mrsm(c, d, n))


DEBUG = True


def main():

    rsa = RSA()
    e, d, n = rsa.genkey(1 << 512, 1 << 514)

    # print d

    if DEBUG:
        msg = TESTCASE
    else:
        msg = raw_input()

    msg_list = []

    i = 0
    LEN = 100
    # value of LEN determined by length of p and q
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
        cryptograph.append(rsa.encrypt(m, e, n))

    plaintext = []

    # decryption
    for c in cryptograph:
        plaintext.append(rsa.decrypt(c, d, n))

    re = ''
    for m in plaintext:
        re += (m)

    if DEBUG:
        print msg_list
        print cryptograph
        print plaintext
        print re

    if msg == re:
        print "You did it!"

if __name__ == '__main__':
    main()
