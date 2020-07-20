import sys
inpy = [int(x) for x in sys.stdin.read().split()]
n = inpy[0]
arr = inpy[1:]
res = []
for i in range(n - 1, -1, -1):
    x = []
    for j in range(i):
        if arr[j] > arr[i]:
            x.append((arr[j],  j))
    x.sort()
    for a, j in x:
        res.append((j + 1, i + 1))
print(len(res))
for i, j in res:
    print(i, j)


     


    

