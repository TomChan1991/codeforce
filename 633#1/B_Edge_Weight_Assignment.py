import collections 
n1 = input()
n = int(n1)
if n == 2: 
    print(1, 1)
    exit()
edges = [set() for _ in range(n)]
for i in range(n - 1):
    x = input()
    a, b = x.split(' ')
    a, b = int(a), int(b)
    edges[a-1].add(b-1)
    edges[b-1].add(a-1)
ocnt = collections.deque()
for i in range(n):
    if len(edges[i]) == 1:
        ocnt.append(i)
nl = set()
 
for i in ocnt:
    for j in edges[i]:
        nl.add(j)
 
x = ocnt[0]
que, l = collections.deque([(-1, x)]), 1
lo = 1
while que:
    size = len(que)
    for _ in range(size):
        p, top = que.popleft()
        if len(edges[top]) == 1 and l % 2 == 0:
            lo = 3
            break
        for j in edges[top]:
            if j != p:
                que.append((top, j))
    l += 1
 
hi = n - len(ocnt) + len(nl) - 1
print(lo, hi)