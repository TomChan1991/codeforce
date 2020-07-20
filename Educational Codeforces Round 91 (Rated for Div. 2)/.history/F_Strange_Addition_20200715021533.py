import sys
class node:
    def __init__(self, _l, _r, _p, _pp, _v, _ppp, _nr, _nl):
        l, r, p, pp, v, ppp = _l, _r, _p, _pp, _v, _ppp
        nl, nr = _nl, _nr
inpy = [x for x in sys.stdin.read().split()]
n, m = int(inpy[0]), int(inpy[1])
s = list(int(i) for i in inpy[2])
index = 3
def build(l, r):
    if l == r:
        return node(l, l, 1, 1, s[l] + 1, 0, None, None)
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
    return node(l, r, p, pp, v, ppp, nr, nl)

def update(index, v, root):
    if index == root.l and index == root.r:
        root.v = v
        return
    mid = (root.l + root.r) // 2
    if index <= root.l:
        update(index, v, root.nl)
    else:
        update(index, v, root.nr)
    nl, nr = root.nl, root.nr 
    root.v = nl.v * nr.v # quanbu
    root.p = nl.v * nr.p # qu wei 
    root.pp = nl.pp * nr.v # qutou
    root.ppp = nl.pp * nr.p # qutouquwei
    if s[mid] == 1:
        root.v += nl.p * nr.pp * (19 - (s[mid] * 10 + s[mid + 1]))
        root.p += nl.p * nr.ppp * (19 - (s[mid] * 10 + s[mid + 1]))
        root.pp += nl.ppp * nr.pp * (19 - (s[mid] * 10 + s[mid + 1]))
        root.ppp += nl.ppp * nr.ppp * (19 - (s[mid] * 10 + s[mid + 1]))
    return

root = build()
print(root.v)


# for i in range(m):
#     a, b = int(inpy[index]), int(inpy[index + 1])
#     index += 2
#     s[a - 1] = b
#     # print(s)
#     pre, p, pp = 9, 1, 0
#     for c in reversed(s):
#         # print(p, pp, 'p')
#         cur = (c + 1) * p
#         # print(cur)
#         if c == 1:
#             cur += max(19 - (c * 10 + pre), 0) * pp
#         pre = c
#         pp, p = p % 998244353 , cur % 998244353 
#     print(p)
