import sys
import collections
inpy = [int(x) for x in sys.stdin.read().split()]
n = inpy[0]
memo = [set() for _ in range(n + 1)]
for i in range(1, len(inpy), 2):
    memo[inpy[i]].add(inpy[i+1])
    memo[inpy[i+1]].add(inpy[i])
# print(memo)
que = collections.deque([(1, 0, 1)])
x = 0
while que:
    index, pre, color = que.pop()
    x += color
    for i in memo[index]:
        if i != pre:
            que.append((i, index, color ^ 1))
print (min(x, n - x) - 1) 
