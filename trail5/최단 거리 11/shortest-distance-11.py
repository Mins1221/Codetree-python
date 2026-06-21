import sys
import heapq
input = sys.stdin.readline
INF = 10**18
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))
A, B = map(int, input().split())
def dijkstra(start):
    dist = [INF] * (N + 1)
    pq = []
    dist[start] = 0
    heapq.heappush(pq, (0, start))
    while pq:
        cur_dist, cur = heapq.heappop(pq)
        if cur_dist > dist[cur]:
            continue
        for nxt, cost in graph[cur]:
            new_dist = cur_dist + cost
            if new_dist < dist[nxt]:
                dist[nxt] = new_dist
                heapq.heappush(pq, (new_dist, nxt))
    return dist
dist_from_A = dijkstra(A)
dist_from_B = dijkstra(B)
shortest = dist_from_A[B]
for i in range(1, N + 1):
    graph[i].sort()
path = [A]
cur = A
while cur != B:
    for nxt, cost in graph[cur]:
        if dist_from_A[cur] + cost == dist_from_A[nxt] and dist_from_A[nxt] + dist_from_B[nxt] == shortest:
            path.append(nxt)
            cur = nxt
            break
print(shortest)
print(*path)
