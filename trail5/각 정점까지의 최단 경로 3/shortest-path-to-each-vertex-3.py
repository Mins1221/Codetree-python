import heapq
import sys
n,m = map(int,input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
INT_MAX = sys.maxsize
dist = [INT_MAX]*(n+1)
visited= [False]*(n+1)
graph = [[] for _ in range(n+1)]
pq = []
for u,v,w in edges:
    graph[u].append((v,w))
dist[1] = 0
heapq.heappush(pq,(0,1))
while pq:
    min_dist, index = heapq.heappop(pq)
    if not visited[index]:
        visited[index] = True
        for v,w in graph[index]:
            if min_dist + w < dist[v]:
                dist[v] = min_dist + w
                heapq.heappush(pq,(dist[v],v))
for i in range(2,n+1):
    if dist[i] == INT_MAX:
        print(-1)
    else:
        print(dist[i])