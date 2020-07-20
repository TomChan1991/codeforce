import sys
inpy = [int(x) for x in sys.stdin.read().split()]
n, m = inpy[0], inpy[1]
belong = inpy[2: 2 + n]

qur = []
for i in range(m - 1):
    qur.append((inpy[i * 2 + 2 + n], inpy[i * 2 + 3 + n]))

contain = [[] for _ in range(m + 1)]
res = 0
for i in range(n -1):
    if belong[i] != belong[i+1]:
        res += 1
    contain[belong[i]].append(i)

contain[belong[-1]].append(n-1)
# print(contain)
print(res)
for i, j in qur:
    print(contain[j])
    for x in contain[j]:
        if x > 0 and belong[x - 1] == i:
            res -= 1
        if x + 1 < n and belong[x + 1] == i:
            res -= 1
        belong[x] = i
        contain[i].append(x)
    contain[j] = []
    print(contain[i])
    print(res)
