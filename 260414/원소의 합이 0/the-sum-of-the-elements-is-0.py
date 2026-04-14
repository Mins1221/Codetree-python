n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))
d1 = {}
d2 = {}
# Please write your code here.'
ans = 0
for i in A:
    for j in B:
        sum1 = i + j
        d1[sum1] = d1.get(sum1, 0) + 1

for k in C:
    for l in D:
        sum2 = -(k + l)
        if sum2 in d1:
            ans += d1[sum2]

print(ans)
