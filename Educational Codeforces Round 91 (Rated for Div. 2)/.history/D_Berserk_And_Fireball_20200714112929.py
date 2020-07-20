import sys
inpy = [int(x) for x in sys.stdin.read().split()]
n, m, x, k, y  = inpy[0:5]
a, b = inpy[5:5+n], inpy[5+n:]
memo = [-1] * m
appear = [[] for _ in range(26)] * 26
for i in range(m):
    appear[m[i]].appear(i)
i, j = 0, 0
while i < n:
    

