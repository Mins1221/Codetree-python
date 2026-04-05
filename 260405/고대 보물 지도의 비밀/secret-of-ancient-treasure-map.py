n, k = map(int, input().split())
A= list(map(int, input().split()))
INF = float('inf')
dp = [[-INF] * (k+2) for _ in range(n+1)]
# Please write your code here.
for i in range(n):
    for j in range(k+1):
        if j <= k:
            if A[i] >= 0 :
                dp[i][j] = max(A[i], dp[i-1][j] + A[i])
            else :
                dp[i][j] = max(A[i], dp[i-1][j-1]+ A[i])

ans = 0
for i in range(n):
    for j in range(k+1):
        ans = max(ans,dp[i][j])

print(ans)