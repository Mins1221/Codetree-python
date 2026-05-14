import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = [
    list(map(int, input().split())) for _ in range(n)
]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]


def bfs(d):
    visit = [[False] * n for _ in range(n)]
    ans = 0
    #시작 위치
    for r in range(n):
        for c in range(n):
            if visit[r][c]:
                continue

            cnt = 0
            queue = deque([(r, c)])

            while queue:
                y, x = queue.popleft()

                if visit[y][x]:
                    continue

                cnt += 1
                visit[y][x] = True

                for i in range(4):
                    ny, nx = y + dy[i], x + dx[i]

                    if 0 <= ny < n and 0 <= nx < n and abs(arr[ny][nx] - arr[y][x]) <= d and not visit[ny][nx]:
                        queue.append((ny, nx))
            
            ans = max(ans, cnt)
            if ans >= (n * n + 1) // 2:
                return True
    
    return False


left, right = 0, 1000000
ans = sys.maxsize

while left <= right:
    mid = (left + right) // 2

    if bfs(mid):
        right = mid - 1
        ans = min(ans, mid)
    else:
        left = mid + 1

print(ans)
