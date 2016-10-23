# -*- coding: utf-8 -*-
'''

@author Lyle
version 6-15

this is my cryptography toolkit

todo:
    need check boundary conditions
    some function need simplify
'''

from random import randint
from base64 import b16encode, b16decode

smallprime = [2, 3, 5, 7, 11, 13, 17, 19, 23]
smallprime += [29, 31, 37, 41, 43, 47, 53, 59]
smallprime += [61, 67, 71, 73, 79, 83, 89, 97]


def calxy(p):
    '''
    let x^2 + y^2 = p
    return x, y
    '''
    if p % 8 != 5:
        return 0, 0

    x = mrsm(2, (p-1)/4, p)
    x -= p if x > p/2 else 0
    y = 1
    m = (x*x + y*y) / p

    while m != 1:
        # print "m:",m
        u, v = x % m, y % m
        if u > m/2:
            u -= m
        if v > m/2:
            v -= m
        # print "u,v",u,v
        x, y = (u*x+v*y)/m, (u*y-v*x)/m
        # print "x,y",x,y
        m = (x*x + y*y) / p
    return x, y


def congruence(a, b, m):
    '''solve Congruence ax % m = b'''
    am = gcd(a, m)
    mam = m/am
    bam = b/am
    aami = inverse(a/am, mam)
    return map(lambda i: (bam*aami+i*mam) % m, range(am))


def crt(b, m):
    '''chinese remainder theorem'''
    product = 1
    for i in m:
        product *= i
    M = []
    for i in m:
        M.append(product/i)
    M_ = []
    length = len(m)
    for i in range(length):
        M_.append(inverse(M[i], m[i]))
    x = 0
    for i in range(length):
        x += b[i]*M[i]*M_[i]
        x %= product
    return x


def euler(x):
    '''calc euler(x)'''

    if isPrime(x):
        return x-1

    count = 1

    for i in range(2, x):
        if gcd(x, i) == 1:
            count += 1

    return count


def euler_v2(x):
    '''sencond version of euler function'''

    l = primeFactor(x, True)

    for i in l:
        x /= i
        x *= (i-1)

    return x


def euler_v3(n):
    '''
    third version of euler
    if need calc many numbers' euler
    this function could be useful
    '''

    isPrime = {}
    primeList = []
    phi = {}  # phi[n] means euler(x)

    for i in range(2, n+1):
        try:
            isPrime[i]
        except:
            primeList.append(i)
            phi[i] = i-1
        for j in range(len(primeList)):
            if i * primeList[j] > n:
                break
            isPrime[i * primeList[j]] = False
            if i % primeList[j] == 0:
                # n%p==0 => phi(n*p) = phi(n) * p
                phi[i * primeList[j]] = phi[i] * primeList[j]
                break
            else:
                # n%p!=0 => phi(n*p) = phi(n) * (p-1)
                phi[i * primeList[j]] = phi[i] * (primeList[j] - 1)

    return phi[n]


def Eratoshenes(n):
    '''
    this function need many memory
    use Eratoshenes to generate prime list
    '''
    composite = set()
    prime = []

    for i in range(2, n+1):
        if i not in composite:
            prime.append(i)
            j = 2
        while j * i <= n:
            composite.add(i*j)
            j += 1

    return prime


def Euclidean(x, y):
    '''
    return s,t
    s*x + t*y = gcd(x,y)
    '''
    if not ((isinstance(x, int) or isinstance(x, long))
            and (isinstance(y, int) or isinstance(y, long))):
        raise TypeError('Only accept integer, please!')

    if x <= 0 or y <= 0:
        raise ValueError('Use positive number, please!')

    flag = True
    if x < y:
        x, y = y, x
        flag = False

    # init
    q, t = x/y, x
    x, y = y, x % y
    s, t, u, v = 1, 0, 0, 1

    while y != 0:
        s, t = t, -q*t + s
        u, v = v, -q*v + u
        q = x/y
        x, y = y, x % y

    if flag:
        return [t, v]
    else:
        return [v, t]


def factorlist(n):
    '''
    return factor list of n
    only could can calc small number
    '''
    return filter(lambda i: n % i == 0, xrange(2, n+1))


def Fermat(n, t=64):
    '''
    Fermat prime number check
    t is security factor
    '''
    if n < 1000:
        return isPrime(n)

    for i in smallprime:
        if n % i == 0:
            return False

    for i in range(t):
        b = randint(2, n-2)
        if gcd(b, n) != 1 or mrsm(b, n-1, n) != 1:
            return False
    return True


def gcd(x, y):
    '''Calculate the Greatest Common Divisor of x and y'''
    while y:
        x, y = y, x % y
    return x


def generatePrime(a, b):
    '''
    generate a prime number between a and b
    '''
    while True:
        p = randint(a, b)
        if Miller_Rabin(p):
            return p


def inverse(a, p):
    '''
    inverse * a = 1 mod p
    '''
    return Euclidean(a, p)[0] % p


def Jacobi(a, m):
    '''
    Jacobi symbol
    if exist a x satisfy x^2 % m = n => return 1
    if return -1 => there isn't such x
    '''

    # divide a into a = 2**n * b
    # calc Jacobi(2,m) ** n * Jacobi(b,m)
    # could be more fast
    # rewrite later

    a %= m

    if a == 0:
        return 0
    elif a == 1:
        return 1
    elif a == -1:
        return 1 if (m-1) % 4 == 0 else -1
    elif a == 2:
        return 1 if (m**2 - 1) % 16 == 0 else -1

    if m % 2 == 1 == a % 2:
        return pow(-1, (m-1)*(a-1)/4)*Jacobi(m, a)

    p = 1
    i = 3

    while m != 1:
        while m % i == 0:
            p *= Legendre(a, i)
            m /= i
        i += 2
    return p


def Legendre(a, p):
    '''
    Legendre symbol
    return 1 if exist which satisfy x^2 % p = a
    else return -1
    '''
    a %= p

    if a == 0:
        return 0
    elif a == 1:
        return 1
    elif a == p-1:
        return 1 if p % 4 == 1 else -1
    elif a == 2:
        return 1 if (p**2 - 1) % 16 == 0 else -1

    if isPrime(a) and isPrime(p) and a != p:
        return 1 if pow(-1, (p-1)*(a-1)/4)*Legendre(p, a) == 1 else -1

    return 1 if mrsm(a, (p-1)/2, p) == 1 else -1


def lcm(a, b):
    '''least common multiple'''
    return a*b/gcd(a, b)


def mrsm(b, n, m):
    '''
    Modular repeat square remainder algorithm
    return b^n % m
    '''
    a = 1

    b %= m
    i = map(int, bin(n)[2:][::-1])
    for k in i:
        a = (a*b**k) % m
        b = (b*b) % m
    return a


def Miller_Rabin(n, t=64):
    '''
    Miller_Rabin prime judge
    t is security factor
    '''
    if n < 1000:
        return isPrime(n)

    for i in smallprime:
        if n % i == 0:
            return False

    u = n - 1
    s = 0
    while (u % 2) == 0:
        u /= 2
        s += 1

    for i in range(t):

        a = randint(2, n-2)
        x = mrsm(a, u, n)

        if x == 1 or x == n-1:
            continue

        for k in range(s-1):
            x = (x*x) % n
            if x == n-1:
                break

        if x != n-1:
            return False

    return True


def modLinearEquationGroup(m, r):

    M = m[0]
    R = r[0]

    for i in range(1, len(m)):
        d = gcd(M, m[i])
        c = r[i] - R
        if (c % d):
            return -1
        k2, k1 = Euclidean(M / d, m[i] / d)
        k1 = (c / d * k1) % (m[i] / d)
        R = R + k1 * M
        M = M / d * m[0]
        R %= M

    return R


def msg2num(msg):
    '''transer str to num'''
    return int(b16encode(msg), 16)


def num2msg(num):
    '''transer num to str'''
    return b16decode((hex(num))[2:].strip('L').upper())


def indList(g, m):
    '''
    return ind list of m
    don't check g and m here
    '''
    p = 1
    ind = []
    for i in range(euler(m)):
        p = (p*g) % m
        ind.append(p)
    return ind


def isPrime(n):
    '''an ordinary function use to judge prime'''
    # 0x8000 don't take so much means
    if n < 2:
        return False

    for i in smallprime:
        if n % i == 0:
            if n == i:
                return True
            return False

    if n > 0x8000:
        return Miller_Rabin(n)

    # 101 because max(smallprime) < 101
    i = 101
    while (i*i) <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def ordam(a, m):
    '''
    calc ord
    a ^ ordam(a,m) == 1
    '''
    i = 1
    while i < m:
        if mrsm(a, i, m) == 1:
            return i
        i += 1
    return 0


def ord4Prime(a, p):
    '''
    calc ord for prime
    need (p-1)/2 is prime
    and a%p != 0,1,-1
    '''
    if isPrime(p) and isPrime((p-1)/2) and (a % p not in (0, 1, p-1)):
        if mrsm(a, (p-1)/2, p) == 1:
            return (p-1)/2
        else:
            return p-1
    else:
        print "Error: wrong use, need p and (p-1)/2 is prime"

    return ordam(a, p)


def primitiveRoot(x):
    '''
    return one primitive root of x
    if x >> long int
    can't use range
    '''
    phi = euler(x)

    i = 2

    while i < x:
        if ordam(i, x) == phi:
            return i
        i += 1

    return 0

def primitiveRootRand4Prime(p):
    '''
    return a rand primitive root of prime p
    '''
    g = p - 1
    while True:
        d = randint(1, g)
        if gcd(d, g) == 1:
            return mrsm(g, d, p)


def primitiveRootList(x):
    '''
    return primitive root list of x
    '''
    phi = euler(x)
    g = primitiveRoot(x)

    return [] if g == 0 else sorted(
        map(lambda i: mrsm(g, i, x),
            filter(lambda i: gcd(i, phi) == 1, range(1, phi))))


def primeFactor(x, dinstinct=False):
    '''
    return prime factor of x
    if dinstict == True
    will only return dinstinct prime number
    '''
    factor = []
    for prime in smallprime:
        while (x % prime) == 0:
            factor.append(prime)
            x /= prime

    while x > 1:
        while (x % prime) == 0:
            factor.append(prime)
            x /= prime
        prime += 2

    return sorted(list(set(factor))) if dinstinct else factor


def reduced_residues(n):
    # return reduced residues system
    return filter(lambda i: gcd(i, n) == 1, range(1, n))


def squareRootModp(a, p):
    '''
    calc x which satisfy x^2 % p = a
    '''
    if Legendre(a, p) != 1:
        raise ValueError("no root here")

    s = p-1
    while s % 2 != 0:
        s /= 2

    n = 3
    while Legendre(n, p) != -1:
        n += 1

    inver = inverse(a, p)
    b = mrsm(n, s, p)
    x = mrsm(a, (s+1)/2, p)

    for i in range(n):
        if (mrsm((inver*x*x), 2**(n-i-1), p)) == -1:
            x *= mrsm(b, 2**(i), p)
    return x


def squareRootModp4(a, p):
    '''
    calc x which satisfy x^2 % p = a
    need p % 4 = 3
    '''

    if p % 4 != 3 or not isPrime(p):
        raise ValueError("could only cal root of prime which mod 4 = 3")

    if Legendre(a, p) != 1:
        raise ValueError("no root here")

    x = mrsm(a, (p+1)/4, p)
    return x


def Solovay_Stassem(n, t=64):
    '''
    Solovay Stassem prime number check
    t is security number
    '''
    if n < 1000:
        return isPrime(n)

    for i in smallprime:
        if n % i == 0:
            return False

    for i in range(t):
        b = randint(2, n-2)
        r = mrsm(b, (n-1)/2, n)
        if (r != 1 and r != n-1) or r != Jacobi(b, n):
            return False

    return True

if __name__ == '__main__':
    pass
