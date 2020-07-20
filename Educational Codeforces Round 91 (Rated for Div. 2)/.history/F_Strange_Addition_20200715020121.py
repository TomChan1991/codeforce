import sys
class node:
    def __init__(self, _l, _r, _p, _pp, _v):
        l, r, p, pp, v = _l, _r, _p, _pp, _v
inpy = [x for x in sys.stdin.read().split()]
n, m = int(inpy[0]), int(inpy[1])
s = list(int(i) for i in inpy[2])
index = 3
def build(l, r):
    if l == r:
        return node(l, l, 1, 1, s[i] + 1)
    mid = (l + r) // 2
    nl, nr = build(l, mid), build(mid + 1, r)
    v = nl.v * nr.v
    if s[mid] == 1:
        v += nl.p * nr.pp * (19 - (s[mid] * 10 + s[mid + 1])
    p = nl.



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
