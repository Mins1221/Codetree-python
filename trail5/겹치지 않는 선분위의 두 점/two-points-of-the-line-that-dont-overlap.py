import sys
input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())  # ← N(점 개수), M(선분 개수) 순서!
    segments = []
    for _ in range(M):
        l, r = map(int, input().split())
        segments.append((l, r))
    segments.sort()

    def can_place(d):
        count = 0
        last = -10**18
        for l, r in segments:
            pos = max(l, last + d)
            if pos > r:
                continue
            pts = (r - pos) // d + 1
            count += pts
            last = pos + (pts - 1) * d
            if count >= N:
                return True
        return count >= N

    lo, hi = 1, 2 * 10**9
    ans = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if can_place(mid):
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1

    print(ans)  # 출력: 2

solve()