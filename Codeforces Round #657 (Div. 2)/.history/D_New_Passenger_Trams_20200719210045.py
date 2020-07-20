import sys
import collections
inpy = [int(x) for x in sys.stdin.read().split()]
n, h, m, k = inpy[:4]
rm = [0] * n
index = 4
for i in range(n):
    rm[i] = (inpy[index+1], i)
    index += 2

res, cancle = 0, None
rm.sort()
s1, s2 = 0, 0
r1 = (rm[0][0] + m - k) % m
r2 = (rm[0][0] + m // 2 - k) % m


