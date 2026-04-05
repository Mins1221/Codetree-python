n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.

dp = [[0] * (n+1) for _ in range(n+1)]

for i in range(n-1, -1, -1):
    for j in range(n-1, -1, -1):
        if B[j] < A[i] :
            dp[i][j] = max(dp[i+1][j+1], B[j]+dp[i][j+1])
        elif A[i] < B[j] : 
            dp[i][j] = max(dp[i+1][j+1], dp[i+1][j])
        else :
            dp[i][j] = dp[i+1][j+1]

print(dp[0][0])