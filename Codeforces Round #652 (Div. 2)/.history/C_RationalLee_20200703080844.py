t = int(input())
for _i in range(t):
    n, k = map(int, input().split())
    a = [int(i) for i in input().split()]
    w = [int(i) for i in input().split()]
    a.sort()
    w.sort()
    e, res = n - k, sum(a[n - k:])
    j = 0
    for i in w:
        if i == 1:
            j += 1
            res += a[-j]
            continue
        e -= i - 1
        res += a[e]
    print(res)
