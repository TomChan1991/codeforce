line = input()
t = int(line)
for _ in range(t):
    line = input()
    a, b, c = [int(i) for i in line.split(' ')]
    ra, rb = -1, -1
    if a  < c:
        ra = 1
    if a * b > c:
        rb = b
    print(ra, ' ', rb)