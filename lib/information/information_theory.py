from math import log, ceil
from decimal import Decimal


def entropy(x):
    '''
    calc entropy with a given list
    '''
    return sum(map(lambda i: - i*log(i, 2), x))


def Shanon(p):
    if abs(sum(p) - 1) > 1e-6:
        print "Error data."
        return p

    p.sort(reverse=True)

    l = map(lambda i: ceil(-log(i, 2)), p)
    accu = [sum(p[0:i]) for i in range(len(p))]
    return [dec_to_bin(accu[i], l[i]) for i in range(len(p))]


def dec_to_bin(num, bit):
    """
    Convert a binary number (<1.0) to a binary format
    """
    if num == 0:
        return '0'*int(bit)
    dec = Decimal(str(num))
    ret = ""
    for i in range(int(ceil(bit))):
        dec *= 2
        t = int(dec)
        dec -= t
        ret += str(t)
    return ret


def Fano(p):
    if abs(sum(p) - 1) > 1e-6:
        print "Error data."
        return p

    p.sort(reverse=True)

    ret = map(lambda i: '', p)

    return reFano(p, ret)


def reFano(p, ret):
    # Fano_Recursion

    if len(p) == 1:
        return ret

    s = sum(p)
    i = 0

    while sum(p[:i]) <= s/2:
        i += 1

    if sum(p[:i]) + sum(p[:i-1]) > s:
        # equals sum(p[:i]) - s/2 > s/2 - sum(p[:i-1])
        i -= 1

    for k in range(len(p)):
        ret[k] += ['1', '0'][k < i]

    return reFano(p[:i], ret[:i]) + reFano(p[i:], ret[i:])


def main():
    # print Shanon([0.05, 0.25, 0.10, 0.15, 0.20, 0.25])
    # print dec_to_bin(0.5, 3.0)
    print Fano([0.01, 0.1, 0.15, 0.17, 0.18, 0.19, 0.2])
    while False:
        print entropy(input())

if __name__ == '__main__':
    main()
