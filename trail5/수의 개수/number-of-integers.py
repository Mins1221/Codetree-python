n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [int(input()) for _ in range(m)]


def lower(arr, t):
    l, r = 0, n
    while l < r:
        mid = (l+r)//2
        if arr[mid] >= t:
            r = mid
        else:
            l = mid + 1
    return l
def upper(arr, t):
    l, r = 0, n
    while l< r:
        mid = (l+r)//2

        if arr[mid] > t:
            r = mid
        else:
            l = mid + 1
    return l      
for t in queries:
    left = lower(arr, t)
    right = upper(arr, t)
    ans = right - left
    print(ans)


