#!/usr/bin/env python
# -*- coding: utf-8 -*-


def Bacon(x, type=0, C=5, t='AB'):
    '''bacon decrypt

    Args:
        x (str): str
        type (int, optional): different of bacon encrypt
        C (int, optional): could be 5, 7, 8 in according to encode
        t (str, optional): different types of encode

    Returns:
        str: decode str list
    '''

    from string import maketrans
    from string import lowercase
    from string import uppercase

    l = ''
    m = ''
    # l,m => different condition

    if type == 0:
        a = lowercase
        a += uppercase
        d = '0' * 26 + '1' * 26
        trantab = maketrans(a, d)
        l = x.translate(trantab)
        l = filter(lambda i: i in '01', l)
    elif type == 1:
        l = x.translate(maketrans(t, '01'))
        l = filter(lambda i: i in '01', l)

    m = l.translate(maketrans('01', '10'))

    re = ['', '']

    if C == 5:
        for i in range(len(l)/C):
            re[0] += chr(eval('0b'+l[i*C:(i+1)*C])+ord('a'))
            re[1] += chr(eval('0b'+m[i*C:(i+1)*C])+ord('a'))
    else:
        for i in range(len(l)/C):
            re[0] += chr(eval('0b'+l[i*C:(i+1)*C]))
            re[1] += chr(eval('0b'+m[i*C:(i+1)*C]))

    return re


if __name__ == '__main__':
    TESTCASE = "DEath IS JUST A PaRT oF lIFE,"
    TESTCASE += "sOMeTHInG wE'RE aLL dESTInED TO dO"
    print(Bacon(TESTCASE))
