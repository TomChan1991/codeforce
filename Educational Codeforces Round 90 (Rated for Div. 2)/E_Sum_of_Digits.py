line = input()
t = int(line)
def helper(n):
    res = '' if n % 9 == 0 else str(n % 9)
    res += '9' * (n // 9)
    return res
for _ in range(t):
    line = input()
    n, k = [int(i) for i in line.split(' ')]
    res = ''
    if k == 0:
        print(helper(n))
    else:
        k += 1
        a = sum(range(k))
        for i in range(10):
            r = n - a
            a = a - i + ((i + k) % 10)
            if r < 0:
                continue
            elif i + k - 1 < 10:
                if r % k != 0:
                    continue
                cur = helper(r // k) + str(i)
                if not res or len(res) > len(cur) or (len(res) == len(cur) and res > cur):
                    res = cur
            else:
                ten = (i + k - 1) % 10 + 1
                last = str(i)
                while r >= ten:
                    if (r - ten) % k == 0:
                        if r - k * 9 + (k - ten) <= 0:
                            cur = helper((r - ten) // k) + last
                        else:
                            cur = helper((r - k * 9 + (k - ten)) //k) + '8' + last
                        if not res or len(res) > len(cur) or (len(res) == len(cur) and res > cur):
                            res = cur
                        break
                    else:
                        last = '9' + last
                        r -= (k - ten) * 9
        if res:
            print(res)
        else:
            print(-1)
