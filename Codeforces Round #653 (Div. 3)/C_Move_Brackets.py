line = input()
t = int(line)
for j in range(t):
    line = input()
    line = input()   
    l, r, cur = 0, 0, 0
    for i in line:
        
        if i == '(':
            cur -= 1
        elif i == ')':
            cur += 1
        l = max(l, cur)
    cur = 0
    for i in reversed(line):
        if i == '(':
            cur += 1
        elif i == ')':
            cur -= 1
        r = max(r, cur)
    print(min(r, l))

        