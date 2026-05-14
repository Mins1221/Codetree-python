import sys
INT_MIN = -sys.maxsize
n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
max_sum = INT_MIN
def is_possible(k):
    max_sum = INT_MIN
    for elem in arr:
        result =elem // k 
        max_sum += result

    if max_sum >= m:
        return True
left = 1
right = max(arr)
ans = INT_MIN
while left <= right:
    mid = (left + right) //2
    if is_possible(mid):
        left = mid +1
        ans = mid
    else:
        right = mid -1
print(ans)
