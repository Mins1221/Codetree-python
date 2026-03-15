n = int(input())
max_num = 1000
mod = 10007
# Please write your code here.
dp = [0] * max_num
dp[1] = 1 
dp[2] = 3
dp[3] = 5 

for i in range(4, (n+1)):
    dp[i] = (dp[i-1] + 2* dp[i-2]) % mod

print(dp[n])

