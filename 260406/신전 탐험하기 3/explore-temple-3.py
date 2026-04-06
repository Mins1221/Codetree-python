n, m = map(int, input().split())
a = [[0]]  # 더미
a += [[0] + list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dp = [[0 for _ in range(m+1)] for _ in range(n+2)]

for i in range(1,n+1):
    for j in range(1,m+1):
        for k in range(1,m+1):
            if j != k :
                dp[i+1][k] = max(dp[i + 1][k] , dp[i][j] + a[i][k])
ans = max(dp[n+1][1:m+1])

print(ans)
