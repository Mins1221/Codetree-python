n = int(input())
a = [[0 for _ in range(4)] for _ in range(n+1)]
for i in range(1,n+1):
    a[i][1],a[i][2],a[i][3] = map(int,input().split())

dp = [[0 for _ in range(4)] for _ in range(n+1)]

for i in range(n):
    for j in range(4):
        for k in range(4):
                if j != k:
                    dp[i+1][k] = max(dp[i+1][k], dp[i][j] + a[i+1][k]) 


if dp[1][j] != dp[n][j]:
    ans = max(dp[n])
print(ans)