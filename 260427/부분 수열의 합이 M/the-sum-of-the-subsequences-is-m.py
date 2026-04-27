import sys
n, m = map(int, input().split())
A = list(map(int, input().split()))
INT_MAX = sys.maxsize
dp = [INT_MAX]*(m+1)
dp[0] = 0
for i in range(n):
    for j in range(m,-1,-1):
        if j >= A[i]:           
            dp[j] = min(dp[j],dp[j-A[i]]+1)

ans = dp[m]
if ans ==INT_MAX:
    ans = -1

print(ans)