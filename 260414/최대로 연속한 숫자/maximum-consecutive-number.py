from sortedcontainers import SortedSet

n, m = map(int, input().split())
nums = list(map(int, input().split()))

by_left = SortedSet()  # (left, length) — 구간 탐색용
by_len  = SortedSet()  # (length, left) — 최댓값 조회용

def add(l, r):
    if l > r: return
    ln = r - l + 1
    by_left.add((l, ln))
    by_len.add((ln, l))

def remove(l, ln):
    by_left.remove((l, ln))
    by_len.remove((ln, l))

add(0, n)

for k in nums:
    # k를 포함하는 구간 찾기
    idx = by_left.bisect_right((k, float('inf'))) - 1
    l, ln = by_left[idx]
    r = l + ln - 1

    remove(l, ln)
    add(l, k - 1)
    add(k + 1, r)

    print(by_len[-1][0] if by_len else 0)