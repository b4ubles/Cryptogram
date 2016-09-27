from cryptography import *
from unit_test import TESTCASE


class Rabin():

    """docstring for Rabin"""

    def __init__(self):
        self.FLAG = 100
        #super(Rabin, self).__init__()
        #self.arg = arg

    # change a little to make it fit rabin
    def genkey(self, a, b):
        while True:
            # print "try p \t"
            p = randint(a, b)
            if p % 4 != 3:
                continue
            if Miller_Rabin(p):
                break

        while True:
            # print "try p \t"
            q = randint(a, b)
            if q % 4 != 3 or q == p:
                continue
            if Miller_Rabin(q):
                break

        return p, q

    def encrypt(self, m, n):
        return ((msg2num(m)*self.FLAG)**2) % n

    def decrypt(self, i, p, q):
        re = self.sqrt(i, p, q)
        for i in re:
            if i % self.FLAG == 0:
                return num2msg(i/self.FLAG)
                # plaintext.append(j)

    def sqrt(self, c, p, q):
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

# if DEBUG == True , will print some information
DEBUG = True
#DEBUG = False


def main():

    rabin = Rabin()
    p, q = rabin.genkey(1 << 512, 1 << 514)
    n = p*q
    # public key : n
    # private key : (p, q)

    if p % 4 != 3 or q % 4 != 3:
        print "error!"
        return

    if DEBUG:
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
        cryptograph.append(rabin.encrypt(m, n))

    plaintext = []

    # decryption
    for i in cryptograph:
        plaintext.append(rabin.decrypt(i, p, q))

    re = ''
    for m in plaintext:
        re += str(m)

    if DEBUG:
        print msg_list
        print cryptograph
        print "plain", plaintext
        print re

    if msg == re:
        print "You did it!"

if __name__ == '__main__':
    main()