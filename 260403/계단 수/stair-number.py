import sys

n = int(input())
dp = [[0]*10 for _ in range(n+1)]
# Please write your code here.
def initialize():
    for j in range(1,10):
        dp[1][j] = 1
    dp[1][0] = 0

initialize()

for i in range(2,n+1):
    for j in range(0,10):
        if j == 0:
            dp[i][j] = dp[i-1][1] 
        elif j == 9:
            dp[i][j] = dp[i-1][8] 
        else :
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1])
MOD = 10**9 +7
ans = sum(dp[n]) % MOD
print(ans)

