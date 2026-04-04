A = input()
B = input()

# Please write your code here.
dp = [[0 for _ in range(len(B)+1)] for _ in range(len(A)+1)
        ]

def initialize():
    dp[1][1] = 1 if A[1] == B[1] else 2

    for i in range(2,len(A)+1):
        if A[i-1] == B[0] :
            dp[i][1] = i
        else:
            dp[i][1] = dp[i-1][1] +1
    for j in range(2,len(B)+1):
        if A[0] == B[j-1]:
            dp[1][j] = j
        else:
            dp[1][j] = dp[1][j-1] +1

initialize()

for i in range(2,len(A)+1):
    for j in range(2,len(B)+1):
        if A[i-1] == B[j-1] :
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + 1

print(dp[len(A)][len(B)] //2)