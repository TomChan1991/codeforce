line = input()
t = int(line)
for _ in range(t):
    line = input()
    n = int(line)
    line = input()
    nums = [int(i) for i in line.split(' ')]
    evensum, oddsum = [0] * (n + 1), [0] * (n + 1)
    for i in range(n):
        evensum[i + 1] = evensum[i] + (nums[i] if i % 2 == 0 else 0)
        oddsum[i + 1] = oddsum[i] + (nums[i] if i % 2 == 1 else 0)
    res = evensum[-1]
    minD = 9999999999
    for i in range(0, n + 1, 2):
        res = max(res, evensum[-1] + (oddsum[i] - evensum[i]) - minD)
        minD = min(minD, oddsum[i] - evensum[i])
        # print(minD)
    minD = 9999999999
    # print('x', res)
    for i in range(1, n + 1, 2):
        res = max(res, evensum[-1] + (oddsum[i] - evensum[i]) - minD)
        minD = min(minD, oddsum[i] - evensum[i])
    print(res)




