import sys
inpy = [x for x in sys.stdin.read().split()]
t = int(inpy[0])
index = 1
mod = "abacaba" 

for _ in range(t):
    n = int(inpy[index])
    s = inpy[index + 1]
    index += 2
    s1 = s.find(mod) 
    print(s1)
    if s1 == -1:
        for i in range(n - 6):
            flag = True
            for j in range(7):
                if s[i+j] != mod[j]:
                    flag = False
                    break
            if flag:
                if i + 11 <= n and s[i+7:i+11] == 'caba': 
                    flag = False
                if flag:
                    s = list(s)
                    s[i:i + 7] = list(mod)
                    for j in range(n):
                        if s[i] == '?':
                            s[i] = 'z'
                    print('yes')
                    print(''.join(s))
                    break
        if i == n - 6:
            print('no')
    else:
        s1 = s[s1 + 1:].find(mod)
        print(s1)
        if s1 == -1:
            s = list(s)
            for j in range(n):
                if s[i] == '?':
                    s[i] = 'z'
            print(s)
            print('yes')
            print(''.join(s))
        else:
            print('No')
                
                    



