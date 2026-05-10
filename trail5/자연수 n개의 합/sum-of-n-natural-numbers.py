import sys
INT_MIN = -sys.maxsize
s = int(input())


left = 1
right = s
max_num = INT_MIN
while left <= right:
    mid = (left + right) //2
    if mid * (mid +1) //2 <= s:
        left = mid +1
        max_num = max(max_num,mid)
    else:
        right = mid -1

print(max_num)