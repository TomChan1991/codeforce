t = int(input())
memo = [0] * (2 * 10 ** 6 + 1)
memo[3] = 4
mod = 
for i in range(3, len(memo)):
    memo[i] = max(4 + memo[i-2], 2 * memo[i - 2] + memo[i-1])
    memo[i] = memo[i] % 
for _i in range(t):
    print(memo[int(input())])
