import sys
n = int(input())
arr = [0] + list(map(int, input().split()))
dp = [0]*(n+1)
INT_MIN = -sys.maxsize
# Please write your code here.

def initialize():
    for i in range(1,n+1):
        dp[i] = -100

    dp[1] = arr[1]
        
initialize()

for i in range(2,n+1):
    dp[i] = max(arr[i],dp[i-1]+arr[i])

ans= -1000
for i in range(1,n+1):
    ans = max(ans,dp[i])

print(ans)



