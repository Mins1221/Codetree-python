import sys
INT_MAX = sys.maxsize
n, k, b = tuple(map(int, input().split()))
arr = [0] *(n+1)
prefix_sum = [0] *(n+1)

def get_sum(s,e):
    return prefix_sum[e] - prefix_sum[s-1]

ans = INT_MAX

for _ in range(b):
    x = int(input())

    arr[x] = 1

prefix_sum[0] = 0

for i in range(1,n+1):
    prefix_sum[i] = prefix_sum[i-1] + arr[i]

for i in range(1,n-k +2):
    ans = min(get_sum(i,i+k-1),ans)

print(ans)