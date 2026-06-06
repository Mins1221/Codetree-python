N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]
l, r = 1, max(arr)
ans = 0
while l <= r:
    mid = (l + r) // 2
    cnt = sum(x // mid for x in arr)

    if cnt >= M:
        ans = mid
        l = mid + 1
    else:
        r = mid - 1

print(ans)
