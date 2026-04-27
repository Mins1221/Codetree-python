import sys
n,m = map(int, input().split())
coin = [0] + list(map(int, input().split()))
INT_MAX = sys.maxsize
dp = [INT_MAX] *(m+1)
dp[0] = 0

for i in range(1,m+1):
    for j in range(1,n+1):
        if i>=coin[j]:
            if dp[i-coin[j]] ==INT_MAX:
                continue
            dp[i] = min(dp[i],dp[i-coin[j]]+1)

ans = dp[m]
if ans ==INT_MAX:
    print(-1)
print(ans)
