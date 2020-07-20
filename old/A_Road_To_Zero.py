
line = input()
t = int(line)
for _ in range(t):
    line = input()
    x, y = (int(i) for i in line.split(' '))
    line = input()
    a, b = (int(i) for i in line.split(' '))
    res = abs(x) * a + abs(y) * a
    if x * y < 0:
        print(res)
    else:
        print(min((min(x, y) * b + abs(x - y) * a), res))




