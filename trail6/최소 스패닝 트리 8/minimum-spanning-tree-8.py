import sys
import heapq
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
input = sys.stdin.readline
for _ in range(m):
    a,b,w = map(int,input().split())
    graph[a].append((w,b))
    graph[b].append((w,a))
pq = []
heapq.heappush(pq,(0,1))
ans =0
visited = [False]*(n+1)
while pq:
    w,node = heapq.heappop(pq)
    if visited[node]:
        continue
    visited[node] = True
    ans += w
    for next_w, next_node in graph[node]:
        if not visited[next_node]:
            heapq.heappush(pq,(next_w,next_node))
print(ans)