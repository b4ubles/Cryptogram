from cry_test import TESTCASE
from AES_SBOX import s_box, inv_sbox


# mode refer to 128bits, 192bits, 256bits
# Nk = 8, Nr = 14 here
# Nb Number of columns (32-bit words) comprising the State.
# For this standard, Nb = 4.
mode = 256
Nk = mode / 32
Nr = Nk + 6
Nb = 4


def key_expansion(w):

    for i in range(Nk, 4*(Nr+1)):
        tmp = [w[4*(i-1)+k] for k in range(4)]

        if i % Nk == 0:
            tmp = sub_bytes(rot_word(tmp))
            tmp = coef_add(tmp, Rcon(i/Nk))
        elif Nk > 6 and i % Nk == 4:
            tmp = sub_bytes(tmp)

        w += bytearray([(w[4*(i-Nk)+k] ^ tmp[k]) for k in range(4)])

    return w


def rot_word(w):
    return w[1:] + w[:1]


def coef_add(a, b):
    for i in range(4):
        a[i] ^= b[i]
    return a


def Rcon(i):
    R = bytearray([0x02, 0x00, 0x00, 0x00])
    if i == 1:
        R[0] = 0x01  # x^(1-1) = x^0 = 1
    elif i > 1:
        R[0] = 0x02
        i -= 1
        while i-1 > 0:
            R[0] = gmult(R[0], 0x02)
            i -= 1
    return R


def gmult(a, b):

    p = 0
    i = 0
    hbs = 0

    for i in range(8):
        if b & 1:
            p ^= a

        hbs = a & 0x80
        a <<= 1
        if (hbs):
            a ^= 0x1b  # 0000 0001 0001 1011
        b >>= 1

    return p % 256


def add_round_key(state, w, r):

    for c in range(Nb):
        for i in range(4):
            state[Nb*i+c] ^= w[4*Nb*r+4*c+i]

    return state


def sub_bytes(s):
    return map(lambda i: s_box[i], s)


def inv_sub_bytes(s):
    return map(lambda i: inv_sbox[i], s)


def shift_rows(state):
    for i in range(1, 4):
        state[Nb*i: Nb*(i+1)] = state[Nb*i + i: Nb*(i+1)] + \
            state[Nb*i: Nb*i + i]
    return state


def inv_shift_rows(state):
    for i in range(1, 4):
        state[Nb*i: Nb*(i+1)] = state[Nb*i + 4-i: Nb*(i+1)] + \
            state[Nb*i: Nb*i + 4-i]
    return state


def mix_columns(state):
    # matrix multiply
    a = bytearray([0x02, 0x01, 0x01, 0x03])
    col = bytearray(4)
    res = bytearray(4)

    for j in range(Nb):
        for i in range(4):
            col[i] = state[Nb*i+j]

        res = coef_mult(a, col, res)

        for i in range(4):
            state[Nb*i+j] = res[i]

    return state


def inv_mix_columns(state):

    a = bytearray([0x0e, 0x09, 0x0d, 0x0b])
    col = bytearray(4)
    res = bytearray(4)

    for j in range(Nb):
        for i in range(4):
            col[i] = state[Nb*i+j]

        res = coef_mult(a, col, res)

        for i in range(4):
            state[Nb*i+j] = res[i]

    return state


def coef_mult(a, b, d):
    d[0] = gmult(a[0], b[0]) ^ gmult(a[3], b[1]) ^ gmult(
        a[2], b[2]) ^ gmult(a[1], b[3])
    d[1] = gmult(a[1], b[0]) ^ gmult(a[0], b[1]) ^ gmult(
        a[3], b[2]) ^ gmult(a[2], b[3])
    d[2] = gmult(a[2], b[0]) ^ gmult(a[1], b[1]) ^ gmult(
        a[0], b[2]) ^ gmult(a[3], b[3])
    d[3] = gmult(a[3], b[0]) ^ gmult(a[2], b[1]) ^ gmult(
        a[1], b[2]) ^ gmult(a[0], b[3])
    return d


def encrypt(m, w):
    state = bytearray(4*Nb)

    for i in range(4):
        for j in range(Nb):
            state[Nb*i+j] = m[i+4*j]

    state = add_round_key(state, w, 0)

    for r in range(1, Nr):
        state = add_round_key(mix_columns(shift_rows(sub_bytes(state))), w, r)

    state = add_round_key(shift_rows(sub_bytes(state)), w, Nr)

    for i in range(4):
        for j in range(Nb):
            m[i+4*j] = state[Nb*i+j]
    return m


def decrypt(c, w):

    state = bytearray(4*Nb)

    for i in range(4):
        for j in range(Nb):
            state[Nb*i+j] = c[i+4*j]

    state = add_round_key(state, w, Nr)

    for r in range(Nr-1, 0, -1):
        state = inv_mix_columns(
            add_round_key(inv_sub_bytes(inv_shift_rows(state)), w, r))

    state = add_round_key(inv_sub_bytes(inv_shift_rows(state)), w, 0)

    for i in range(4):
        for j in range(Nb):
            c[i+4*j] = state[Nb*i+j]

    return c


def byteprint(b):
    s = ''
    for i in b:
        s += hex(i)[2:]
    print s


def genKey(x):
    x = sha256(x)
    return bytearray([int(x[i*2:i*2+2], 16) for i in range(len(x)/2)])


def sha256(s):
    return __import__('hashlib').sha256(str(s)).hexdigest()

DEBUG = True
# DEBUG = False


class AES:

    """A simple AES encrpt class"""

    def __init__(self, key, mode=32):
        '''
        init here, input a str as key
        mode means byte
        32 = 256 bits encrypt
        '''
        self.key = key_expansion(genKey(key))
        self.mode = mode

    def encrypt(self, plain):
        e = bytearray()
        plain += '\x00' * (32 - (len(plain) % 32))
        plain = bytearray(plain)
        for i in range(len(plain)/32):
            e += (encrypt(plain[i*32:(i+1)*32], self.key))
        return e

    def decrypt(self, c):
        d = bytearray()
        for i in range(len(c)/32):
            d += (decrypt(c[i*32:(i+1)*32], self.key))
        return str(d).rstrip('\x00')


def main():

    if DEBUG:
        aes = AES(raw_input('your key: '))
        plain = raw_input('your plain: ')
    else:
        aes = AES('This is a secret key, 23333')
        plain = TESTCASE

    cryptograph = aes.encrypt(plain)
    re = aes.decrypt(cryptograph)

    if DEBUG:
        print 'plain: ', plain
        print 'cry: ', cryptograph

    if plain == re:
        print "You did it!"

if __name__ == '__main__':
    main()
