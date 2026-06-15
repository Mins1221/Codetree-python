import sys
sys.setrecursionlimit(100000)
n, r, q = tuple(map(int, input().split()))
edges = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
size = [0] * (n + 1)
for _ in range(n - 1):
    x, y = tuple(map(int, input().split()))
    edges[x].append(y)
    edges[y].append(x)
def dfs(x):
    size[x] = 1
    for y in edges[x]:
        if visited[y]: 
            continue
        visited[y] = True
        dfs(y)
        size[x] += size[y]
visited[r] = True
dfs(r)
for _ in range(q):
    x = int(input())
    print(size[x])

