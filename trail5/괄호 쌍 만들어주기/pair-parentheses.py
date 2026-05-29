import sys
INT_MAX = sys.maxsize
A = input()
n = len(A)
R = [0] *(n+1)

for i in range(n-2,-1,-1):
    R[i] = R[i+1]
    if A[i] == ')' and A[i+1] == ')':
        R[i] +=1

ans = 0
for i in range(n-2):
    if A[i] == '(' and A[i+1] == '(':
        ans += R[i+2]

print(ans)