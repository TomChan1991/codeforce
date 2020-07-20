line = input()
t = int(line)
for i in range(t):
    line = input()
    x, y, n = [int(i) for i in line.split(' ')]
    r = n - n % x + y 
    print(r if r <= n else r - x)
