import sys
INT_MAX = sys.maxsize
n, m = map(int, input().split())
graph= [
    [0]*(n+1)  
    for _ in range(n+1)
    ]
visited = [False] * (n+1)

dist = [INT_MAX] * (n+1)

for _ in range(m):
    x,y,z = tuple(map(int,input().split()))
    graph[x][y] = z if graph[x][y] == 0 else min(graph[x][y],z)
    graph[y][x] = z if graph[y][x] == 0 else min(graph[y][x],z)

dist[1] = 0
ans = 0
for i in range(1,n+1):
    min_index = -1
    for j in range(1,n+1):
        if visited[j] :
            continue
        if min_index == -1 or dist[min_index] > dist[j]:
            min_index = j
    visited[min_index] = True

    ans += dist[min_index]

    for j in range(1,n+1):
        if graph[min_index][j] == 0:
            continue
        dist[j] = min(dist[j] , graph[min_index][j])

print(ans)

