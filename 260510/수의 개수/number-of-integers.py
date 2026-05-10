n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [int(input()) for _ in range(m)]

def lower_bound(i):
    left = 0
    right = n-1
    lower_idx = n
    while left <= right :
        mid = (left+right) //2
        if arr[mid] >= i:
            lower_idx = min(lower_idx,mid)
            right = mid -1
        else:
            left = mid +1
    return lower_idx
def upper_bound(i):
    left = 0
    right = n-1
    upper_idx = n
    while left <= right :
        mid = (left+right) //2
        if arr[mid] > i:
            upper_idx = min(upper_idx,mid)
            right = mid -1
        else:
            left = mid +1
    return upper_idx

for i in queries:
    lower_idx = lower_bound(i)
    upper_idx = upper_bound(i)
    ans = upper_idx - lower_idx
    print(ans)