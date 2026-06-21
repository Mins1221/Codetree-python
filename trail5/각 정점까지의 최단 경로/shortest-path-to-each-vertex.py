import sys
import heapq
input = sys.stdin.readline
N, M = map(int, input().split())
K = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, weight = map(int, input().split())
    graph[a].append((b, weight))
    graph[b].append((a, weight))
INF = int(1e18)
dist = [INF] * (N + 1)
dist[K] = 0
pq = []
heapq.heappush(pq, (0, K))  
while pq:
    current_dist, current_node = heapq.heappop(pq)
    if current_dist > dist[current_node]:
        continue
    for next_node, weight in graph[current_node]:
        next_dist = current_dist + weight
        if next_dist < dist[next_node]:
            dist[next_node] = next_dist
            heapq.heappush(pq, (next_dist, next_node))
for i in range(1, N + 1):
    if dist[i] == INF:
        print(-1)
    else:
        print(dist[i])
