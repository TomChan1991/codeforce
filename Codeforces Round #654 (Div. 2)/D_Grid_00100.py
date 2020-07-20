t = int(input())
for _ in range(t):
    n, k = [int(i) for i in input().split()]
    if k % n == 0:
        print(0)
    else:
        print(2)
    r = k % n
    s = k // n + 1
    for i in range(n):
        if r == 0:
            s -= 1
        if i + s > n:
            print(('1' * (i + s - n)) + ('0' * (n - s)) + ('1' * (n-i)))
        else:
            print(('0' * i) + ('1') * (s) + ('0' * (n - s - i)))
        r -= 1