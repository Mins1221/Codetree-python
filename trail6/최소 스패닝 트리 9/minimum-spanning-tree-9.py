import sys
import heapq
n,m = map(int,input().split())
input = sys.stdin.readline
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,w = map(int,input().split())
    graph[a].append((w,b))
    graph[b].append((w,a))
pq =[]
heapq.heappush(pq,(0,1))
visited= [False]*(n+1)
ans = 0
count = 0
while pq:
    w,node = heapq.heappop(pq)
    if visited[node]:
        continue
    visited[node] = True
    ans +=w
    count +=1
    for next_w,next_node in graph[node]:
        if not visited[next_node]:
            heapq.heappush(pq,(next_w,next_node))
print(ans)

