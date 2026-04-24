import sys
INT_MAX = sys.maxsize
n,k,b = tuple(map(int,input().split()))
arr = [0] *(n+1)
prefix_sum = [0] * (n+1)
for i in range(b):
    x = int(input())
    arr[x] = 1

for i in range(n):
    prefix_sum[i] = prefix_sum[i-1] + arr[i]
ans = INT_MAX
for i in range(1,n-k+2):
    ans = min(ans,prefix_sum[i+k+1]-prefix_sum[i-1])

print(ans)