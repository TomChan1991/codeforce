# t = int(input())
# memo = [0] * (2 * 10 ** 6 + 1)
# memo[3] = 4
# mod = int(10 ** 9 + 7)
# for i in range(4, len(memo)):
#     memo[i] = max(4 + memo[i-2] + 4 * memo[i - 3] + 4 * memo[i - 4], 2 * memo[i - 2] + memo[i-1])
#     memo[i] = memo[i] % mod
# for _i in range(t):
#     print(memo[int(input())])

v = []
v.append(0)
v.append(0)
v.append(0)
v.append(4)
v.append(4)
mod = int(1e9+7)
for i in range (5, 2000010):
    v.append(max(((2*v[i-2])+v[i-1])%mod,((4*v[i-4])+4*v[i-3]+v[i-2]+4)%mod))
t = int(input())
for _ in range(t):
    print(v[int(input())])
