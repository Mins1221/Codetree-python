from sortedcontainers import SortedSet

n, m = map(int, input().split())
nums = list(map(int, input().split()))

iv_right = {}   # left -> right
iv_left  = {}   # right -> left
starts   = SortedSet()   # 구간 왼쪽끝
by_len   = SortedSet()   # (길이, 왼쪽끝) — 최댓값을 [-1]로 조회

# 초기 구간 [0, n]
iv_right[0] = n
iv_left[n]  = 0
starts.add(0)
by_len.add((n + 1, 0))

for k in nums:
    idx = starts.bisect_right(k) - 1
    l = starts[idx]
    r = iv_right[l]

    # 기존 구간 제거
    del iv_right[l], iv_left[r]
    starts.remove(l)
    by_len.remove((r - l + 1, l))

    # [l, k-1] 구간 추가
    if l <= k - 1:
        iv_right[l]    = k - 1
        iv_left[k - 1] = l
        starts.add(l)
        by_len.add((k - l, l))

    # [k+1, r] 구간 추가
    if k + 1 <= r:
        iv_right[k + 1] = r
        iv_left[r]      = k + 1
        starts.add(k + 1)
        by_len.add((r - k, k + 1))

    print(by_len[-1][0] if by_len else 0)