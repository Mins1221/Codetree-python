import sys
INT_MAX = sys.maxsize
n = int(input())
graph = [[0] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)
dist = [INT_MAX] * (n+1)
for i in range(1,n+1):
    graph[0][i] = int(input())
for i in range(1,n+1):
    graph[i] = [0] + list(map(int,input().split()))
dist[0] = 0 
ans = 0
for i in range(0,n+1):
    min_index = -1
    for j in range(0,n+1):
        if visited[j]:
            continue
        if min_index == -1 or dist[min_index] > dist[j]:
            min_index = j
    visited[min_index] = True
    ans += dist[min_index]
    for j in range(1,n+1):
        dist[j] = min(dist[j],graph[min_index][j])
print(ans)

