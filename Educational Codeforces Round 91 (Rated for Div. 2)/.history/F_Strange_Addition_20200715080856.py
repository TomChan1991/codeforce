import sys
mod = 10 ** 10
class node:
    def __init__(self):
        self.p1, self.p2, self.p3 = 0, 0, 0
        self.nl, self.nr = None, None
    def l(self):
        return self.p1 % mod
    def r(self):
        return self.p1 // mod
    def p(self):
        return self.p2 % mod
    def pp(self):
        return self.p2 // mod
    def ppp(self):
        return self.p3 % mod
    def v(self):
        return self.p3 // mod
    def setP(self, l, r):
        self.p1 = r * mod + l
    def setV(self, v, p, pp, ppp):
        self.p2 = pp * mod + p
        self.p3 = v * mod + ppp
inpy = [x for x in sys.stdin.read().split()]
n, m = int(inpy[0]), int(inpy[1])
s = list(int(i) for i in inpy[2])
index = 3

def cal(root):
    print('b', root.l(), root.r())
    mid = (root.l + root.r) // 2
    nl, nr = root.nl, root.nr
    # print(nl, nr)
    print(mid)
    v = nl.v() * nr.v() # quanbu
    p = nl.v() * nr.p() # qu wei 
    pp = nl.pp() * nr.v() # qutou
    ppp = nl.pp() * nr.p() # qutouquwei
    print('c')
    if s[mid] == 1:
        v += nl.p() * nr.pp() * (19 - (s[mid] * 10 + s[mid + 1]))
        p += nl.p() * nr.ppp() * (19 - (s[mid] * 10 + s[mid + 1]))
        pp += nl.ppp() * nr.pp() * (19 - (s[mid] * 10 + s[mid + 1]))
        ppp += nl.ppp() * nr.ppp() * (19 - (s[mid] * 10 + s[mid + 1]))
    v %= 998244353 
    p %= 998244353
    pp %= 998244353
    ppp %= 998244353
    root.setV(v, p, pp, ppp)




def build(l, r):
    print(l, r)
    if l == r:
        x = node()
        x.setP(l, l)
        x.setV(s[l] + 1, 1, 1, 0)
        return x
    mid = (l + r) // 2
    nl, nr = build(l, mid), build(mid + 1, r)
    # print(nl, nr)
    root = node()
    root.nl, root.nr = nl, nr
    root.setP(l, r)
    print('a')
    cal(root)
    return root
 
def update(index, v, root):
    if index == root.l and index == root.r:
        root.v = v
        return
    mid = (root.l + root.r) // 2
    # print(mid)
    if index <= mid:
        update(index, v, root.nl)
    else:
        update(index, v, root.nr)
    cal(root)
    return
 
root = build(0, n - 1)
print(root.v(), 'x')
 
 
for i in range(m):
    a, b = int(inpy[index]), int(inpy[index + 1])
    index += 2
    s[a - 1] = b
    # print(a, b)
    update(a-1, b+1, root)
    # print(s)
    # pre, p, pp = 9, 1, 0
    # for c in reversed(s):
    #     # print(p, pp, 'p')
    #     cur = (c + 1) * p
    #     # print(cur)
    #     if c == 1:
    #         cur += max(19 - (c * 10 + pre), 0) * pp
    #     pre = c
    #     pp, p = p % 998244353 , cur % 998244353 
    print(root.v())