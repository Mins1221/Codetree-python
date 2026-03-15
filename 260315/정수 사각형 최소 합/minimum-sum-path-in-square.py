
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
# Please write your code here.
dp = [
    [0 for _ in range(n)]
      for _ in range(n)
]

def initialze():
    dp[0][n-1] = grid[0][n-1]

    for i in range(1,n):
        dp[i][n-1] = dp[i-1][n-1] + grid[i][n-1]

    for i in reversed(range(n-1)):   
        dp[0][i] = dp[0][i+1] + grid[0][i]

initialze()

for i in range(1,n):
    for j in reversed(range(n-1)):  
        dp[i][j] = min(dp[i-1][j] + grid[i][j], dp[i][j+1]+ grid[i][j])



print(dp[n-1][0])

