#!/usr/bin/env python
# -*- coding: utf-8 -*-


def fenceEncode(s, t=0):
    '''fence encode function
    '''
    relist = []
    if not t:
        for t in range(2, len(s)//2+2):
            relist.append(fenceEncode(s, t=t))
    else:
        re = ['']*t
        for i in range(len(s)//t+1):
            for j in range(t):
                try:
                    re[j] += s[i*t+j]
                except:
                    break
        return ''.join(re)
    return relist


def fenceDecode(s, t=0):
    '''fence decode function
    '''
    ret = []
    if not t:
        for t in range(2, len(s)//2+1):
            ret.append(fenceDecode(s, t=t))
    else:
        re = ''
        for i in range(len(s)//t):
            for k in range(t):
                re += s[k*(len(s)//t) + i]
        return re
    return ret


if __name__ == '__main__':
    TESTCASE = "}~144_0t_em0c14w{galf"
    s = TESTCASE
    for i in range(2, len(s)//2+2):
        x = fenceEncode(s, t=i)
        print(x, fenceDecode(x, t=i))
