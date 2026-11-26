N, M = map(int, input().split())
coin = list(map(int, input().split()))

INF=M+1
dp = [INF] * (M + 1)
dp[0] = 0

for c in coin:
    for x in range(c, M + 1):
        if dp[x - c] + 1 < dp[x]:
            dp[x] = dp[x - c] + 1

print(dp[M] if dp[M] != INF else -1)