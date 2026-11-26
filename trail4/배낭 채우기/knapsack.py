N, M = map(int, input().split())
dp = [0] * (M + 1)

for _ in range(N):
    w, v = map(int, input().split())
    for j in range(M, w - 1, -1):
        if dp[j - w] + v > dp[j]:
            dp[j] = dp[j - w] + v

print(dp[M])