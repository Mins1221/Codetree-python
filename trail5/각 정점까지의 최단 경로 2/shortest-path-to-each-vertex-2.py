n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
import sys
# Please write your code here.
INT_MAX = sys.maxsize

dist = [[INT_MAX] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dist[i][i] = 0

for i in range(1, m + 1):
    x, y, z = edges[i - 1]
    dist[x][y] = min(dist[x][y], z)

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if dist[i][j] == INF:
            print(-1, end = " ")
        else:
            print(dist[i][j], end = " ")
    print()
