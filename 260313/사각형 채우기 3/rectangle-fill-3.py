n = int(input())

# Please write your code here.
mod = 1000000007
max_num = 1000
dp = [0] * max_num
dp[1] = 2
dp[2] = 7
dp[3] = 22

for i in range(4,n+1):
    dp[i] = (2*dp[i-1] + 4*dp[i-1]) % mod


print(dp[n])