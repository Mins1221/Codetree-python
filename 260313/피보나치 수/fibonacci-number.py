N = int(input())
MAX_NUM = 45
dp = [0] * (MAX_NUM+1)
dp[1] =1
dp[2] =1
# Please write your code here.
for i in range(3, N+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[N])