import sys
import collections
inpy = [int(x) for x in sys.stdin.read().split()]
t = inpy[0]
index = 1
for _ in range(t):
    n = inpy[index]
    index += 1
    f, flag = inpy[index], 1
    index += 1
    for i in range(1, n):
        x = inpy[index]
        index += 1
        if not flag and  x > f:
            flag = 1
        elif flag and x < f:
            flag = 0
    if flag:
        print('YES')
    else:
        print('NO')
