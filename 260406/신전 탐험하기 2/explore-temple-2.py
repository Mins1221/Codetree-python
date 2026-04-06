import sys

n = int(input())
a = [[0 for _ in range(4)] for _ in range(n+1)]
for i in range(1,n+1):
    a[i][1],a[i][2],a[i][3] = map(int,input().split())

dp = [[[0 for _ in range(4)]for _ in range(4)] for _ in range(n+1)]
for j in range(1,4):
    dp[1][j][j] = a[1][j]

for i in range(1,n):
    for j in range(1,4):
        for k in range(1,4):
            for l in range(1,4):
                if k == l:
                    continue
                dp[i+1][j][l] = max(dp[i+1][j][l], dp[i][j][k]+ a[i+1][l])
        
ans =0
for j in range(1,4):
    for k in range(1,4):
        if j ==k:
            continue
        ans = max(ans,dp[n][j][k])
print(ans)
