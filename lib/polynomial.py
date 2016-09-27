class Polynomial:

    '''
    factor should be a list which both contain 
    factor and coefficient of a polynomial

    for example:
    factor = [ [2,3], [1,2] ] represent polynomial
    f(x) = 3x^2 + 2x
    '''

    def __init__(self, factor):

        if isinstance(factor, list):
            for i in factor:
                if isinstance(i, list) and len(i) == 2 \
                        and isinstance(i[0], int) and isinstance(i[1], int):
                    pass
                else:
                    print "wrong init arugment"
                    factor = [[0, 0]]
                    break
        else:
            print "wrong init arugment"
            factor = [[0, 0]]

        factor.sort()
        self.factor = factor

    def __add__(self, other):
        add = []
        i, j = 0, 0

        while True:
            x = self.factor[i]
            y = other.factor[j]

            if x[0] > y[0]:
                add.append(y)
                j += 1
            elif x[0] < y[0]:
                add.append(x)
                i += 1
            elif x[0] == y[0]:
                if x[1]+y[1] != 0:
                    add.append([x[0], x[1]+y[1]])
                i += 1
                j += 1

            if i == len(self.factor):
                while j != len(other.factor):
                    add.append(other.factor[j])
                    j += 1
                break

            if j == len(other.factor):
                while i != len(self.factor):
                    add.append(self.factor[i])
                    i += 1
                break

        return Polynomial(add)

    def __sub__(self, other):
        sub = []
        i, j = 0, 0

        while True:
            x = self.factor[i]
            y = other.factor[j]

            if x[0] > y[0]:
                sub.append([y[0], -y[1]])
                j += 1
            elif x[0] < y[0]:
                sub.append(x)
                i += 1
            elif x[0] == y[0]:
                if x[1]-y[1] != 0:
                    sub.append([x[0], x[1]-y[1]])
                i += 1
                j += 1

            if i == len(self.factor):
                while j != len(other.factor):
                    sub.append(other.factor[j])
                    j += 1
                break

            if j == len(other.factor):
                while i != len(self.factor):
                    sub.append(self.factor[i])
                    i += 1
                break

        return Polynomial(sub)

    def __mul__(self, other):
        x = []
        for i in self.factor:
            for j in other.factor:
                x.append([i[0]+j[0], i[1]*j[1]])
        re = Polynomial(x)
        re.merge()
        return re

    def pow(self):
        return self.factor[-1][1]

    def gcd(self, x, y):
        if x < y:
            x, y = y, x
        while x % y != 0:
            x %= y
            x, y = y, x
        return y

    # bad version, need change
    def getfai(self, x):
        i = 1
        fai = 0
        while i != x:
            if self.gcd(i, x) == 1:
                fai += 1
            i += 1
        return fai

    def __str__(self):
        s = ''
        for i in self.factor[::-1]:
            if i[1] > 0:
                s += ("+"+str(i[1])+"x^"+str(i[0]))
            elif i[1] == 0:
                pass
            else:
                s += (str(i[1])+"x^"+str(i[0]))
        return s

    def cal(self, x):
        result = 0
        for i in self.factor:
            result += i[1]*(x**i[0])
        return result

    def simplify(self, x):
        fai = self.getfai(x)
        for i in self.factor:
            i[1] = i[1] % x
            i[0] = i[0] % fai
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
            if x[j][0] == i[0]:
                x[j][1] += i[1]
            else:
                x.append(i)
                j += 1

        self.factor = []

        for i in x:
            if i[1] != 0:
                self.factor.append(i)

    def derivative(self):
        dx = []
        for i in self.factor:
            dx.append([i[0]-1, i[0]*i[1]])
        return Polynomial(dx)

if __name__ == '__main__':
    x = Polynomial([[2, 3], [3, 7]])
    y = Polynomial([[1, 2], [2, 4]])
    print str(x+y)
    print str(x-y)
    print str(x*y)
