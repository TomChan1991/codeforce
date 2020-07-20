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
s1, s2, e2 = 0, 0, 0
q1 = collections.deque()
q2 = collections.deque()
i = -1

for i in range(1, 2 * n):
    if rm[i][0] < rm[0][0] + k:
        s1 += 1
        q1.append(rm[i][1])
    if rm[i][0] < rm[0][0] + k + m // 2:
        s2 += 1
    if rm[0][0] + m // 2 < rm[i][0] < rm[0][0] + k + m // 2:
        q2.append(rm[i][1])
print(s1, s2, q1, q2)





