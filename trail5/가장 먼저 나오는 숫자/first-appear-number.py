n, m = map(int, input().split())
arr = list(map(int, input().split()))
query = list(map(int, input().split()))

def lower_bound(i):
    left = 0
    right = n-1
    min_idx = n
    while left <= right:
        mid = (left + right) //2
        if arr[mid] >= i:
            min_idx = min(min_idx,mid)
            right = mid -1
        else:
            left = mid +1
    if min_idx != n:
        if arr[min_idx] == i:
            return min_idx +1
        else:
            return -1
    return -1

for i in query:
    ans = lower_bound(i) 
    print(ans)
