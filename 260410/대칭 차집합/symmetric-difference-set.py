n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
sa = set(A)
sb = set(B)
cnt = 0
for elem in A:
    if elem not in sb:
        cnt +=1
for elem in B:
    if elem not in sa:     
        cnt+=1

print(cnt)