import sys
inpy = [int(x) for x in sys.stdin.read().split()]
t = inpy[0]
index = 1
for _ in range(t):
    n, x = inpy[index], inpy[index + 1]
    nums = inpy[index + 2: index + 2 + n]
    index += 2 + n
    nums.sort(reverse=True)
    res, cnt = 0, 0
    for i in nums:
        cnt += 1
        if i * cnt >= x:
            cnt = 0
            res += 1
    print(res)
