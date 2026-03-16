import sys
n = int(input())
arr = list(map(int, input().split()))
INT_MIN = -sys.maxsize
# Please write your code here.
dp = [0] * (n+1)

def initialize():
    for i in range(n):
        dp[i] = INT_MIN

    dp[0] = 0
    
initialize()

for i in range(1,n):
    for j in range(0,i):
        if dp[j] == INT_MIN:
            continue
        if j + arr[j] >= i:
            dp[i] = max(dp[i], dp[j]+1)

ans=0
for i in range(n):
    ans = max(ans,dp[i])

print(ans)