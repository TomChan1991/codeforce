import sys
class node:
    def __init__(self, _l, _r, _p, _pp, _v, _ppp):
        l, r, p, pp, v, ppp = _l, _r, _p, _pp, _v, _ppp
inpy = [x for x in sys.stdin.read().split()]
n, m = int(inpy[0]), int(inpy[1])
s = list(int(i) for i in inpy[2])
index = 3
def build(l, r):
    if l == r:
        return node(l, l, 1, 1, s[l] + 1, 0)
    mid = (l + r) // 2
    nl, nr = build(l, mid), build(mid + 1, r)
    v = nl.v * nr.v # quanbu
    p = nl.v * nr.p # qu wei 
    pp = nl.pp * nr.v # qutou
    ppp = nl.pp * nr.p # qutouquwei
    if s[mid] == 1:
        v += nl.p * nr.pp * (19 - (s[mid] * 10 + s[mid + 1]))
        p += nl.p * nr.ppp * (19 - (s[mid] * 10 + s[mid + 1]))
        pp += nl.ppp * nr.pp * (19 - (s[mid] * 10 + s[mid + 1]))
        ppp += nl.ppp * nr.ppp * (19 - (s[mid] * 10 + s[mid + 1]))
    return node(l, r, p, pp, v, ppp)



for i in range(m):
    a, b = int(inpy[index]), int(inpy[index + 1])
    index += 2
    s[a - 1] = b
    # print(s)
    pre, p, pp = 9, 1, 0
    for c in reversed(s):
        # print(p, pp, 'p')
        cur = (c + 1) * p
        # print(cur)
        if c == 1:
            cur += max(19 - (c * 10 + pre), 0) * pp
        pre = c
        pp, p = p % 998244353 , cur % 998244353 
    print(p)
