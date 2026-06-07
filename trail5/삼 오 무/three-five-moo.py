import sys
INT_MAX = sys.maxsize
n = int(input())
l = 0
r = INT_MAX
ans = INT_MAX

while l <= r:
    mid = (l+r) // 2
    if mid - mid // 3 - mid // 5 + mid // 15 >=n:
        r = mid -1
        ans = min(ans,mid)
    else:
        l = mid + 1

print(ans)