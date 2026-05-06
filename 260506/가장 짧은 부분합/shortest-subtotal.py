import sys
INT_MAX = sys.maxsize
n, s = map(int, input().split())
arr = list(map(int, input().split()))
sum_val = arr[0]
j=0
ans = INT_MAX
for i in range(n):
    while j +1 < n and sum_val < s:
        sum_val +=arr[j+1]
        j+=1

    if sum_val >= s:
        ans = min(ans, j-i+1)

    sum_val -= arr[i]
if ans == INT_MAX:
    ans = -1
print(ans)