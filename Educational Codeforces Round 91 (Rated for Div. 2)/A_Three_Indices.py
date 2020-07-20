t = int(input())
for _ in range(t):
    n = int(input())
    nums = [int(i) for i in input().split()]
    i, j, k = -1, -1, -1
    for x in range(n):
        if i == -1 :
            i = x
        elif j == -1:
            if nums[x] > nums[i]:
                j = x
            else:
                i = x
        else:
            if nums[x] > nums[j]:
                j = x
            else:
                k = x
                break
        # print(x, i, j, k)
    if k == -1:
        print('NO')
    else:
        print('YES')
        print(i + 1, j + 1, k + 1)