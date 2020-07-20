import collections

n, m = map(int, input().split())
w = map(int, input().split())
memo = [set() for _ in range(m)]
p = [[] for _ in range(m + 1)] 
for i in range(i, m + 1):
    x, y = map(int, input().split())
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
while que and len(res) < m:
    x = que.popleft()
    for i, o in memo[x]:
        if i not in exist:
            res.append(i)
        memo[o] += 1
        if memo[o] == 0:
            que.append(o)
if len(res) != m:
    print('DEAD')
else:
    print('ALIVE')
    for i in reversed(res):
        print(i, end=' ') 
    print()





