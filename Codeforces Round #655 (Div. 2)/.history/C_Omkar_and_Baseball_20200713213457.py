import sys
inpy = [int(x) for x in sys.stdin.read().split()]
t = inpy[0]
index = 1
# print(inpy)
for _ in range(t):
    n = inpy[index]
    nums = inpy[index + 1: index + 1 + n]
    # print(n, nums)
    index = index + 1 + n
    sort_nums = sorted(nums)
    start = 0
    for i, j in zip(nums, sort_nums):
        if i != j and start == 0:
            start = 1
        elif i == j and start == 1:
            start = 2
        elif i != j and start == 2:
            start = 3
    if start == 0:
        print(0)
    elif start == 1 or start == 2:
        print(1)
    else:
        print(2)
    
    