import sys
n, m = map(int, input().split())
arr = list(map(int, input().split()))
INT_MAX = sys.maxsize
dp = [0]*  (m+1)
for i in range(m+1):
    dp[i] = INT_MAX 

    dp[0] = 0
for i in range(n):
    for j in range(m,-1,-1):
        if j >= arr[i]:
            dp[j] = min(dp[j],dp[j-arr[i]]+1)

ans = dp[m]

if ans ==INT_MAX:
    ans = -1

print(ans)