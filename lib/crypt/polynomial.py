from cryptography import euler


class X:

    def __init__(self, coe, index):
        self.index = index
        self.coe = coe

    def __neg__(self):
        return X(-self.coe, self.index)

    def __str__(self):

        if self.coe == 0:
            return ''

        coe = self.coe
        index = self.index

        if coe > 1:
            s = "+" + str(coe) 
        elif coe == 1:
            s = "+"
        elif coe == -1:
            s = "-"
        else:
            s = str(coe)

        return s + 'x' + ['^'+str(index), ''][index == 1]

    def __add__(self, other):
        return X(self.coe + other.coe, self.index)

    def __sub__(self, other):
        return X(self.coe - other.coe, self.index)

    def __mul__(self, other):
        return X(self.coe * other.coe, self.index * other.index)


class Polynomial:

    '''
    factor should be a list which both contain 
    factor and coefficient of a polynomial

    for example:
    factor = [ [2,3], [1,2] ] represent polynomial
    f(x) = 3x^2 + 2x
    '''

    def __init__(self, factor=[X(0, 0)]):
        self.factor = sorted(factor, cmp=lambda x, y: x.index < y.index)

    def __add__(self, other):
        add = []
        i, j = 0, 0

        while True:
            x = self.factor[i]
            y = other.factor[j]

            # print x,y

            if x.index > y.index:
                add.append(y)
                j += 1
            elif x.index < y.index:
                add.append(x)
                i += 1
            elif x.index == y.index:
                if x.coe+y.coe != 0:
                    add.append(x+y)
                i += 1
                j += 1

            if i == len(self.factor):
                add += other.factor[j:]
                break

            if j == len(other.factor):
                add += self.factor[i:]
                break

        return Polynomial(add)

    def __sub__(self, other):
        sub = []
        i, j = 0, 0

        while True:
            x = self.factor[i]
            y = other.factor[j]

            if x.index > y.index:
                sub.append(-y)
                j += 1
            elif x.index < y.index:
                sub.append(x)
                i += 1
            elif x.index == y.index:
                if x.coe-y.coe != 0:
                    sub.append(x-y)
                i += 1
                j += 1

            if i >= len(self.factor):
                sub += map(lambda k: -k, other.factor[j:])
                break

            if j >= len(other.factor):
                sub += self.factor[i:]
                break

        return Polynomial(sub)

    def __mul__(self, other):
        x = []
        for i in self.factor:
            for j in other.factor:
                x.append(i * j)
        re = Polynomial(x)
        re.merge()
        return re

    def __div__(self, other):
        # not finish
        return [X(0, 0)]

    def __neg__(self):
        return Polynomial() - Polynomial(self.factor)

    def __str__(self):
        s = ''.join(map(str, self.factor[::-1]))
        return s[s[0] == '+':]

    def cal(self, x):
        result = 0
        for i in self.factor:
            result += i.coe*(x**i.index)
        return result

    def simplify(self, x):
        fai = euler(x)
        for i in self.factor:
            i.coe = i.coe % x
            i.index = i.index % fai
        self.factor.sort()
        self.merge()

    def merge(self):
        x = []
        j = -1
        for i in self.factor:
            if not x:
                x.append(i)
                j += 1
                continue
            if x[j].index == i.index:
                x[j].coe += i.coe
            else:
                x.append(i)
                j += 1

        self.factor = filter(lambda i: i.coe != 0, x)

    def derivative(self):
        dx = []
        for i in self.factor:
            dx.append([i.index-1, i.index*i.coe])
        return Polynomial(dx)

if __name__ == '__main__':
    x = Polynomial([X(3, 2), X(7, 3)])
    y = Polynomial([X(2, 1), X(4, 2)])
    print 'x: ', x
    print 'y: ', y
    print '-x: ', -x
    print 'x + y: ', x+y
    print 'x - y: ', x-y
    print 'x * y: ', x*y
