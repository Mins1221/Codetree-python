import sys
import heapq
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, weight = map(int, input().split())
    graph[a].append((b, weight))
    graph[b].append((a, weight))
A, B = map(int, input().split())
INF = int(1e18)
dist = [INF] * (N + 1)
parent = [-1] * (N + 1)
dist[A] = 0
pq = []
heapq.heappush(pq, (0, A))  
while pq:
    current_dist, current_node = heapq.heappop(pq)
    if current_dist > dist[current_node]:
        continue
    for next_node, weight in graph[current_node]:
        next_dist = current_dist + weight
        if next_dist < dist[next_node]:
            dist[next_node] = next_dist
            parent[next_node] = current_node
            heapq.heappush(pq, (next_dist, next_node))
print(dist[B])
path = []
cur = B
while cur != -1:
    path.append(cur)
    if cur == A:
        break
    cur = parent[cur]
path.reverse()
print(*path)
