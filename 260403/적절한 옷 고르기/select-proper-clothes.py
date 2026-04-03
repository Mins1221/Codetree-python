import sys
INT_MIN = -sys.maxsize
n,m = map(int, input().split())
clothes = [tuple(map(int, input().split())) for _ in range(n)]
s = [0]+[x[0] for x in clothes]
e = [0] +[x[1] for x in clothes]
v = [0] + [x[2] for x in clothes]
dp = [[INT_MIN] *(n+1) for _ in range(m+1)]
# Please write your code here.
def initialize():
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s[j]<= i <=e[j]:
                dp[i][j] = 0

initialize()

for i in range(2,m+1):
    for j in range(1,n+1):
        if s[j] <= i <= e[j]:
            for k in range(1,n+1):
                dp[i][j] = max(dp[i][j], dp[i-1][k] + abs(v[j]-v[k]))
    
ans = 0
for j in range(1,n+1):
    ans = max(ans,dp[i][j])

print(ans)