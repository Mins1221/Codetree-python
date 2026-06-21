import heapq
import sys
INT_MAX = sys.maxsize

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
pq = []

dist = [INT_MAX] * (n+1)
visited = [False] * (n+1)

for _ in range(m):
    x,y,z = tuple(map(int,input().split()))

    graph[x].append((y,z))
    graph[y].append((x,z))

dist[1] = 0

heapq.heappush(pq,(0,1))

ans = 0
while pq:
    min_dist, min_index = heapq.heappop(pq)

    if visited[min_index]:
        continue

    visited[min_index] = True
    ans += min_dist

    for target_index,target_dist in graph[min_index]:
        new_dist = target_dist
        if dist[target_index] > new_dist:
            dist[target_index] = new_dist
            heapq.heappush(pq,(new_dist,target_index))
print(ans)


