n = int(input())
mod = 10007
max_num = 1000
# Please write your code here.
dp =  [0] * max_num

dp[1] = 1
dp[2] = 2
dp[3] = 3
for i in range(4,n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 10007

print(dp[n])

