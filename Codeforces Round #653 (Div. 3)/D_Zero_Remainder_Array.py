line = input()
t = int(line)
for j in range(t):
    line = input()
    n, k = [int(i) for i in line.split(' ')]
    line = input()
    nums = [int(i) for i in line.split(' ')]
    memo = {}
    for i in nums:
        memo[i % k] = memo.get(i % k, 0) + 1
    r, last = 0, 0
    for i, v in memo.items():
        if i == 0:continue
        if v > r:
            r = memo[i]
            last = i
        elif v == r:
            last = min(i, last)
    if r == 0:
        print(0)
    else:
        print(r * k - last + 1)

