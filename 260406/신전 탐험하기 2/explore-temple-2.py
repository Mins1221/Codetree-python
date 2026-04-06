import sys

n = int(input())
a = [[0 for _ in range(4)] for _ in range(n+1)]
for i in range(1,n+1):
    a[i][1],a[i][2],a[i][3] = map(int,input().split())

INF = sys.maxsize
ans = 0

for start in (1,2,3):
    dp = [[-INF] * 4 for _ in range(n+1)]
    dp[1][start] = a[1][start]
    for i in range(1,n):
        for j in range(1,4):
            for k in range(1,4):
                if j != k:
                    dp[i+1][k] = max(dp[i+1][k], dp[i][j] + a[i+1][k]) 

    for i in range(1,4):
        if i != start:
            ans = max(ans,dp[n][i])



print(ans)
