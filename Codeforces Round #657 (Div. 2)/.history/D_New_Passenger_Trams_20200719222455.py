import sys
import collections
inpy = [int(x) for x in sys.stdin.read().split()]
n, h, m, k = inpy[:4]
rm = [0] * n
index = 4
for i in range(n):
    rm[i] = (inpy[index+1], i + 1)
    index += 2

res, cancle = 0, None
rm.sort()
rm = rm + [(i[0] + m, i[1]) for i in rm]
s1, s2, e2 = 0, 0, 0
q1 = collections.deque()
q2 = collections.deque()
res = 99
x = 99999999
   

for i in range(n):
    while s1 < 2 * n:
        if rm[s1][0] < rm[i][0] + k:
            q1.append(rm[s1])
            s1 += 1
        else:
            break
    while s2 < 2 * n:
        if rm[s2][0] < rm[i][0] + m // 2 + k:
            q2.append(rm[s2])
            s2 += 1
        else:
            break
    while q1 and q1[0][0] <= rm[i][0]:
        q1.popleft()
    while q2 and q2[0][0] <= rm[i][0] + m // 2:
        q2.popleft()
    # print(q1, q2, rq1, rq2)
    if x > len(q1) + len(q2):
        res = rm[i][0] + k
        x = len(q1) + len(q2)




print(x, res)
for i in rm:
    if res - k  < rm[i][0] < res or res - k + m // 2  < rm[i][0] < res + m // 2:
        print(rm[i][1])







