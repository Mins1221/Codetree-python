n = int(input())
A= []
B = []

for _ in range(2 * n):
    r, b = map(int, input().split())
    A.append(r)
    B.append(b)

# Please write your code here.

INF = float('inf')
dp = [[-INF] * (n+1) for _ in range(n+1)]
dp[0][0] = 0

for i in range(n+1):
    for j in range(n+1):
        if i >=1:
            dp[i][j] = max(dp[i-1][j]+A[i+j-1],dp[i][j])

        if  j >= 1:
            dp[i][j] = max(dp[i][j],dp[i][j-1]+B[i+j-1])

ans = 0
for i in range(n+1):
    ans = max(ans,dp[i][j])

print(ans)