n, m = map(int, input().split())
edges =[0]+ [tuple(map(int, input().split())) for _ in range(m)]
graph = [[0] *(n+1) for _ in range(n+1)]
import sys
INT_MAX = sys.maxsize
visited = [False] * (n + 1)
dist = [INT_MAX] * (n + 1) 
for i in range(1, m + 1):
    x, y, z = edges[i]
    graph[x][y] = z
dist[1] = 0
for i in range(1, n + 1):
    min_index = -1
    for j in range(1, n + 1):
        if visited[j]:
            continue
        
        if min_index == -1 or dist[min_index] > dist[j]:
            min_index = j
    visited[min_index] = True
    for j in range(1, n + 1):
        if graph[min_index][j] == 0:
            continue

        dist[j] = min(dist[j], dist[min_index] + graph[min_index][j])

for i in range(2, n + 1):
    print(dist[i])


