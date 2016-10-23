from random import randint
from DES_Constant import *

def gen_key():
    return [odd_check(randint(0, 127)) for i in range(8)]


def odd_check(x):
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
    # print map(bin,gen_key())
    # print repalce(range(64), IP)
    print len(repalce(gen_key(), PC1_C))

if __name__ == '__main__':
    main()
