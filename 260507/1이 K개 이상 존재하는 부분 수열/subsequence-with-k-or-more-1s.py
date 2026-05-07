import sys
INT_MAX = sys.maxsize
n, k = map(int, input().split())
arr = [0] + list(map(int, input().split()))
ones = 0
j = 0
ans = INT_MAX

for i in range(1,n+1):
    while j +1 <= n and ones < k :
        j +=1
        if arr[j] ==1:
            ones +=1

    if ones >= k :
        ans = min(ans, j-i+1)

    if arr[i] ==1:
        ones -=1
if ans == INT_MAX:
    ans = -1
print(ans)

