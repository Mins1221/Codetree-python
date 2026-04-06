import sys
A = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()
dp = [[0 for _ in range(len(B)+1)] for _ in range(len(A)+1)]

for i in range(1,len(A)+1):
    for j in range(1,len(B)+1):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else :
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])

ans = []
i = len(A)
j = len(B)
while i>0 and j>0:
    if A[i-1] == B[j-1]:
        ans.append(A[i-1])
        i -=1
        j -=1
    elif dp[i-1][j] >= dp[i][j-1]:
        i -=1
    else:
        j -=1
    
reverse = ans.reverse()
print(''.join(ans))