import sys
import heapq
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
pq= []
input = sys.stdin.readline
for i in range(m):
    a,b,w = map(int,input().split())
    graph[b].append((w,a))
    graph[a].append((w,b))
visited= [False] * (n+1)
heapq.heappush(pq,(0,1))
ans =0
while pq:
    w,node = heapq.heappop(pq)
    if visited[node]:
        continue
    ans +=w
    visited[node] = True
    for next_w, next_node in graph[node]:
        if not visited[next_node]:
            heapq.heappush(pq,(next_w,next_node))
print(ans)