import heapq

line = input()
n, k = (int(i) for i in line.split(' '))
line = input()
num = [int(i) for i in line.split(' ')]
line = input()
c = [int(i) for i in line.split(' ')]
memo = [(c[-1], 999999999)]
pre = c[-1]
for i in range(k - 2, -1, -1):
    if c[i] == pre: continue
    memo.append((c[i] - pre, i + 2))
    pre = c[i]
num.sort(reverse=True)
heap, res = [], []
for i in num:
    if not heap or memo[heap[0][0]][1] <= i:
        heapq.heappush(heap, [0, 0, len(res)])
        res.append([])
    heap[0][1] += 1
    res[heap[0][2]].append(i)
    if heap[0][1] == memo[heap[0][0]][0]:
        x = heapq.heappop(heap)
        x[0] += 1
        x[1] = 0
        if x[0] != len(memo):
            heapq.heappush(heap, x)

print(len(res))
for i in res:
    print(len(i), end=' ')
    for j in i:
        print(j, end=' ')
    print()
