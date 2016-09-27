def fence_encrypt(s, t=0):
    '''
    fence encrypt function
    '''
    relist = []
    if not t:
        for t in range(2, len(s)/2+2):
            relist.append(fence_encrypt(s, t=t))
    else:
        re = ['']*t
        for i in range(len(s)/t+1):
            for j in range(t):
                try:
                    re[j] += s[i*t+j]
                except:
                    break
        return ''.join(re)
    return relist


def fence_decrypt(s, t=0):
    '''
    fence decrypt function
    '''
    ret = []
    if not t:
        for t in range(2, len(s)/2+1):
            ret.append(fence_decrypt(s, t=t))
    else:
        re = ''
        for i in range(len(s)/t):
            for k in range(t):
                re += s[k*(len(s)/t) + i]
        return re
    return ret

if __name__ == '__main__':
    TESTCASE = "HLEICICTSTWOOCFEMCNAO"
    s = TESTCASE
    for i in range(2, len(s)/2+2):
        x = fence_encrypt(s,t=i)
        print x,fence_decrypt(x,t=i)
