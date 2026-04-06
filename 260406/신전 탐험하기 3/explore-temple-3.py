n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(n):
    for j in range(m):
        for k in range(m):
            if j != k :
                dp[i+1][k] = max(dp[i + 1][k] , dp[i][j] + a[i][k])

ans = max(dp[n])

print(ans)

