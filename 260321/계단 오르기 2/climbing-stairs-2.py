import sys
n = int(input())
arr = [0] + list(map(int, input().split()))
INT_MIN = -sys.maxsize
dp = [[0] * 4 for _ in range(n+1)]
def initialize():
    for i in range(n+1):
        for j in range(4):
            dp[i][j] = INT_MIN
    dp[0][0] = 0
initialize()

for i in range(2,n+1):
    for j in range(0,4):
        if dp[i-2][j] != INT_MIN:
            dp[i][j] = max(dp[i][j], dp[i-2][j] + arr[i])
        if j >= 1 and dp[i-1][j-1] != INT_MIN:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + arr[i])

ans = INT_MIN
for i in range(1,n+1):
    ans = max(dp[n])
print(ans)