import sys
import heapq
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    start, end, weight = map(int, input().split())
    graph[start].append((end, weight))
INF = sys.maxsize
dist = [INF] * (n+1)
def dijkstra(start):
    pq = []
    dist[start] = 0
    heapq.heappush(pq, (0, start))
    while pq:
        cur_dist, cur_node = heapq.heappop(pq)
        if cur_dist > dist[cur_node]:
            continue
        for next_node, weight in graph[cur_node]:
            new_dist = cur_dist + weight
            if new_dist < dist[next_node]:
                dist[next_node] = new_dist
                heapq.heappush(pq, (new_dist, next_node))
dijkstra(1)
for i in range(2, n+1):
    if dist[i] == INF:
        print(-1)
    else:
        print(dist[i])
