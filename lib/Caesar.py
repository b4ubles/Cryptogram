def caesar(s):
    from string import maketrans
    from string import lowercase
    from string import uppercase
    l = lowercase
    u = uppercase
    for shift in range(26):
        re = s.translate(maketrans(l, l[shift:]+l[:shift]))
        re = re.translate(maketrans(u, u[shift:]+u[:shift]))
        print re

if __name__ == '__main__':
    s = "o gs rerk"
    #s = raw_input()
    s = s.lower()
    caesar(s)
