# refer: https://en.wikipedia.org/wiki/RC4

from cry_test import TESTCASE


class RC4:

    def __init__(self, k):
        self.key = bytearray(k.encode('hex'))

    def encrypt(self, s):
        return self.keyStream(s).encode('base64')

    def decrypt(self, s):
        return self.keyStream(s.decode('base64'))

    def keyStream(self, s):
        result = ''
        S = range(256)
        T = [self.key[i % len(self.key)] for i in range(256)]

        j = 0
        for i in range(256):
            j = (j + S[i] + T[i]) & 0xff
            S[i], S[j] = S[j], S[i]

        i = j = 0
        for k in range(len(s)):
            i = (i + 1) & 0xff
            j = (j + S[i]) & 0xff
            S[i], S[j] = S[j], S[i]
            result += chr(ord(s[k]) ^ (S[(S[i] + S[j]) & 0xff]))

        return result

# __DEBUG = True
__DEBUG = False


def main():

    if __DEBUG:
        key = raw_input('your key: ')
        plain = raw_input('your plain: ')
    else:
        key = 'This is a secret key, 23333'
        plain = TESTCASE

    rc4 = RC4(key)

    cryptograph = rc4.encrypt(plain)
    re = rc4.decrypt(cryptograph)

    print 'plain: ', plain
    print 'cry: ', cryptograph

    if plain == re:
        print "You did it!"

if __name__ == '__main__':
    main()
