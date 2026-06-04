n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [int(input()) for _ in range(m)]

for i in queries:
    idx = -1
    left = 0
    right = n-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == i:
            idx = mid +1
            break
        if arr[mid] > i :
            right = mid -1
        else:
            left = mid +1
    
    print(idx)