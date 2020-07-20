import collections
import sys
inpy = [int(x) for x in sys.stdin.read().split()]
n, m = inpy[:2]
w = inpy[2: 2 + n]
memo = [set() for _ in range(n)]
p = [[] for _i in range(m + 1)] 
for i in range(1, m + 1):
    x, y = inpy[n + 2 * i: 2 + n + 2 * i]
    memo[x-1].add((i, y - 1))
    memo[y-1].add((i, x - 1))
    w[x-1] -= 1
    w[y-1] -= 1
que = collections.deque()
for i in range(n):
    if w[i] >= 0:
        que.append(i)

res = collections.deque()
exist = [False] * (m + 1)
while que and len(res) <  m:
    x = que.popleft()
    for i, o in memo[x]:
        if not exist[i]:
            res.append(i)
            exist[i] = True
        w[o] += 1
        if w[o] == 0:
            que.append(o)
if len(res) != m:
    print('DEAD')
else:
    print('ALIVE')
    for i in reversed(res):
        print(i, end=' ') 
    print()





