import sys
sys.setrecursionlimit(100000)

n = int(input())
edges = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
dist = [0] * (n + 1)
max_dist = 0
last_node = 0
for _ in range(n - 1):
    x, y = tuple(map(int, input().split()))
    edges[x].append(y)
    edges[y].append(x)
def dfs(x):
    global max_dist, last_node
    for y in edges[x]:
        if visited[y]: 
            continue
        visited[y] = True
        dist[y] = dist[x] + 1
        if dist[y] > max_dist:
            max_dist = dist[y]
            last_node = y
        dfs(y)
visited[1] = True
dfs(1)

for i in range(1, n + 1):
    visited[i] = False
    dist[i] = 0
visited[last_node] = True
dfs(last_node)
print((max_dist + 1) // 2)

