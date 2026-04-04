A = input()
B = input()

# Please write your code here.
dp = [[0 for _ in range(len(B)+1)] for _ in range(len(A)+1)
        ]

def initialize():
    dp[0][0] = 0 

    for i in range(1,len(A)+1):
        
            dp[i][0] = dp[i-1][0] +1
    for j in range(1,len(B)+1):
        
            dp[0][j] = dp[0][j-1] +1

initialize()

for i in range(1,len(A)+1):
    for j in range(1,len(B)+1):
        if A[i-1] == B[j-1] :
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + 1

print(dp[len(A)][len(B)])