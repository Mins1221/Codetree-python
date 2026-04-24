n = int(input())
B = [input() for _ in range(n)]

# Please write your code here.
L,R = [0] *n, [0]*n
ans =0

for shape in "PHS":
    same_cnt = 0
    for i in range(n):
        if B[i] == shape:
            same_cnt +=1

        L[i] = max(L[i],same_cnt)

for shape in "PHS":
    same_cnt = 0
    for i in range(n-1,-1,-1):
        if B[i] == shape:
            same_cnt +=1

        R[i] = max(R[i],same_cnt)

for i in range(0,n-1):
    ans = max(ans,L[i]+R[i+1])

print(ans)