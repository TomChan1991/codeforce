
import sys
import heapq
inpy = [int(x) for x in sys.stdin.read().split()]
n = inpy[0]
for j in range(10, 1000):
    l, r = j // 10, j % 10
    cur = 1
    for i in range(10):
        if r > 0:
            cur = cur * (l + 1)
            r -= 1
        else:
            cur = cur * l
    if cur >= n:
        s = 'codeforces'
        r = j % 10
        for i in range(10):
            if r > 0:
                print(s[i] * (l + 1), end='')
                r -= 1
            else:
                print(s[i] * (l), end='')
        break




    

