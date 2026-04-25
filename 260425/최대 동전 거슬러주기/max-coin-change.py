import sys
n,m= map(int, input().split())
coin = [0] + list(map(int, input().split()))
INT_MIN = -sys.maxsize
dp = [0] * (m+1)
for i in range(m+1):
    dp[i] = INT_MIN

dp[0] = 0
for i in range(1,m+1):
    for j in range(1,n+1):
        if dp[i-coin[j]] == INT_MIN:
            continue
        if i >= coin[j] :
            dp[i] = max(dp[i], dp[i-coin[j]]+1)
        
ans = dp[m]
if ans == INT_MIN:
    print(-1)

print(ans)