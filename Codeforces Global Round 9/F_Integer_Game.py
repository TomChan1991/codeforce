from nbconvert.writers import stdout

a, b, c = map(int, input().split())
print('First')
print(1)
x = 1
stdout.flush()
for i in range(1000):
    n = int(input())
    if n == 1:
        a += x
        x = abs(c- b)
        print(x)    
    elif n == 2:
        b += x
        x = abs(c - a)
    elif n == 3:
        c += x
        x = abs(a - b)
    if a == b or b == c:
        break
    print(x)
    x.flush()
    
    
