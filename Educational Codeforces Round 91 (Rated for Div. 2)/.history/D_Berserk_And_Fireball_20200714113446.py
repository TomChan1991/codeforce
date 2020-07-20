import sys
inpy = [int(x) for x in sys.stdin.read().split()]
n, m, x, k, y  = inpy[0:5]
a, b = inpy[5:5+n], inpy[5+n:]
memo = [-1] * m
appear = {}
for i in range(m):
    if m[i] not in appear:
        appear[m[i]] = set()
    appear[m[i]].append(i)
i, j = 0, 0
while i < n:
    if a[i] in appear:
        for j in appear:
            if j == 0 or memo[j-1] != -1:
                


