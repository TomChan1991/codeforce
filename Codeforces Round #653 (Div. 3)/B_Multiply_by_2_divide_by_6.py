line = input()
t = int(line)
for i in range(t):
    line = input()
    n = int(line)
    c2, c3 = 0, 0
    while n % 2 == 0:
        n = n // 2
        c2 += 1
    while n % 3 == 0:
        n = n // 3
        c3 += 1
    if n != 1 or c2 > c3:
        print(-1)
    else:
        print(2 * c3 - c2)