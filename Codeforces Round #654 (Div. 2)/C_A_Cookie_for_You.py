t = int(input())
for _ in range(t):
    a, b, n, m = [int(i) for i in input().split()]
    if a + b < m + n:
        print('No')
        continue
    if min(a, b) < m:
        print('No')
        continue
    print('Yes')
