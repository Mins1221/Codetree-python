import sys
INT_MAX = sys.maxsize
n, m = tuple(map(int, input().split()))
graph = [
    [0] * (n + 1)
    for _ in range(n + 1)
]
visited = [False] * (n + 1)

dist = [INT_MAX] * (n + 1) 

path = [0] * (n + 1)

for _ in range(m):
    x, y, z = tuple(map(int, input().split()))
    graph[x][y] = z
    graph[y][x] = z

a, b = tuple(map(int, input().split()))
dist[a] = 0

# O(|V|^2) 다익스트라 코드
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

        if dist[j] > dist[min_index] + graph[min_index][j]:
            dist[j] = dist[min_index] + graph[min_index][j]
            path[j] = min_index

print(dist[b])
x = b
vertices = []
vertices.append(x)

while x != a:
    x = path[x]
    vertices.append(x)
for num in vertices[::-1]:
    print(num, end=" ")

