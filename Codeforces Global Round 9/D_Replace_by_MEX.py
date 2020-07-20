import sys
inpy = [int(x) for x in sys.stdin.read().split()]
t = inpy[0]
index = 1
for _i in range(t):
    n = inpy[index]
    index += 1
    arr = inpy[index:index+n]
    index += n
    exist = [0] * (n + 1)
    for i in arr:
        exist[i] += 1
    deal = 0
    res = []
    for _i in range(2 * n):
        mex = 0
        while exist[mex] != 0:
            mex += 1
        if mex == n:
            break
        exist[arr[mex]] -= 1
        exist[mex] += 1
        arr[mex] = mex
        res.append(mex + 1)
    for _i in range(2*n + 1):
        while deal < n : 
            if deal == arr[deal]:
                deal += 1
            else:
                break
        if deal == n:
            break
        flag = True
        mex = 0
        while exist[mex] != 0:
            mex += 1
        exist[mex] += 1
        for i in range(n):
            if arr[i] == deal:
                arr[i] = mex
                res.append(i + 1)
                exist[arr[i]] -= 1
                flag = False
                break
        if flag:
            exist[arr[deal]] -= 1
            arr[deal] = deal
            
            res.append(deal + 1)
    print(len(res))
    for i in res:
        print(i, end=' ')
    print()

        



