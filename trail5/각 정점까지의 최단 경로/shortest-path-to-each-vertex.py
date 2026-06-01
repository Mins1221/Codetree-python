n,m = map(int,input().split())
k = int(input())
edges = [0] + [tuple(map(int,input().split())) for _ in range(m)]
import sys
import heapq
INT_MAX = sys.maxsize
pq = []
graph = [[] for _ in range(n+1)]
dist= [INT_MAX] * (n+1)

for i in range(1,m+1):
    x,y,z = edges[i]
    graph[x].append((y,z))
    graph[y].append((x,z))
dist[k] = 0
heapq.heappush(pq,(0,k))
while pq:
    min_dist, min_index = heapq.heappop(pq)
    if min_dist != dist[min_index]:
        continue
    for target_index, target_dist in graph[min_index]:
        new_dist = dist[min_index] + target_dist
        if dist[target_index] > new_dist:
            dist[target_index] = new_dist
            heapq.heappush(pq,(new_dist,target_index))

for i in range(1,n+1):
    print(-1 if dist[i] ==INT_MAX else dist[i])