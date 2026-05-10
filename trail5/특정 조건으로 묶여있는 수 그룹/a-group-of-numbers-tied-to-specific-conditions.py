n, k = map(int, input().split())
nums = [int(input()) for _ in range(n)]
nums.sort()

import bisect

L = []
for i in range(n):
    n_i = nums[i]
    e_i = max(bisect.bisect_right(nums,n_i+k)-1,i)
    L.append(e_i-i+1)

R = [1] * n
for i in range(n):
    R[n-i-1] = L[n-i-1]
    if i > 0:
        R[n-i-1] = max(R[n-i-1],R[n-i])

ans = -1
for i in range(n):
    if i + L[i] >= n:
        continue
    temp = L[i] + R[i+L[i]]
    if ans < temp:
        ans = temp

print(ans)




