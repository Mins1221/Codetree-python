import sys
input = sys.stdin.readline
n, m = map(int, input().split())
point = []
for _ in range(m):
    a, b = map(int, input().split())
    point.extend(range(a, b + 1))   # 선분 위 정수점을 후보로

def calc(point, k, d):              # k: 놓을 점의 개수 목표
    last = point[0]
    count = 1
    for p in point[1:]:
        if p - last >= d:
            count += 1
            last = p
            if count >= k:
                return True
    return False

point.sort()
low, high = 1, point[-1] - point[0]
ans = 0
while low <= high:
    mid = (low + high) // 2
    if calc(point, n, mid):         # ← m이 아니라 n!
        ans = mid
        low = mid + 1
    else:
        high = mid - 1
print(ans)