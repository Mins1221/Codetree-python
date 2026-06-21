import sys
import heapq
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, d = map(int, input().split())
    graph[b].append((a, d))
INF = int(1e18)
dist = [INF] * (N + 1)
school = N
dist[school] = 0
pq = []
heapq.heappush(pq, (0, school)) 
while pq:
    current_dist, current_node = heapq.heappop(pq)
    if current_dist > dist[current_node]:
        continue
    for next_node, weight in graph[current_node]:
        next_dist = current_dist + weight
        if next_dist < dist[next_node]:
            dist[next_node] = next_dist
            heapq.heappush(pq, (next_dist, next_node))
answer = 0
for i in range(1, N):
    answer = max(answer, dist[i])
print(answer)
