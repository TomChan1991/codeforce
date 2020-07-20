import sys

n = int(input())
res = [0] * (n + 1)
def helper(l, r, x = 0, f = 0):
    if x == 0:
        print('?', l, r)
        sys.stdout.flush()
        x, f = [int(i) for i in input().split()]
    if f == 1:
        res[l] = x
        for i in range(l + 1, r + 1):
            print('?', i, i)
            sys.stdout.flush()
            a, b = [int(i) for i in input().split()]
            res[i] = a
        return 1
    if f == r - l + 1:
        for i in range(l, r + 1):
            res[i] = x
        return f
    end = r - f if f > (r - l) // 2 else (r + l) // 2
    cnt = helper(l, end)
    nstart =  end + 1
    if res[end] == x:
        remain = f - cnt
        while remain > 0 and nstart <= r :
            res[nstart] = x
            nstart += 1
            remain -= 1
        if nstart <= r:
            return helper(nstart, r)
        return f
    if res[end] < x:
        return helper(nstart, r, x, f)
    return helper(nstart, r)


helper(1, n)
print('!', end=' ')
for i in res[1:]:
    print(i, end=' ')
print()



