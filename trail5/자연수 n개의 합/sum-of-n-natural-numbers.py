import sys
INT_MIN = -sys.maxsize
s = int(input())
left = 0
right = s
ans =INT_MIN
while left <= right:
    mid = (left+right) //2
    if (mid * (mid+1)//2) <=s:
        left = mid +1
        ans = max(ans,mid)
    else:
        right = mid -1
print(ans)