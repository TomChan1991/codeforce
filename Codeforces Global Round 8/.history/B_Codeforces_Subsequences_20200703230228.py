
import sys
import heapq
inpy = [int(x) for x in sys.stdin.read().split()]
n = inpy[0]
res = []
i = 2
while n > 1:
    while n % i == 0:
        res.append(i)
        n = n // i
    i += 1

while len(res) > 10:
    x, y = heapq.heappop(res), heapq.heappop(res)
    heapq.heappush(x * y)

s = 
for i in range(10):
