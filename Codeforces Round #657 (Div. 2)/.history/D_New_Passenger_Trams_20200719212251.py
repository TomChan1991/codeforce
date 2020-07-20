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
rm = rm + [(i[0] + m, i[1]) for i in rm]
print(rm)
s1, s2 = 0, 0

i = -1

for i in range(1, 2 * n):
    if rm[i] < rm[0][0] + k:
        s1 += 1;
    if rm[i] < rm[0][0] + k + m // 2:
        s2 += 1
print(s1, s2)





