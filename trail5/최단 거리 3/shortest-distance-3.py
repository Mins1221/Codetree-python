import sys, heapq
INT_MAX = sys.maxsize
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
A, B = map(int, input().split())
graph = [[] * (n + 1) for _ in range(n + 1)]
for edge in edges:
    a, b, c = edge
    graph[a].append((b, c))
    graph[b].append((a, c))

dist = [INT_MAX] * (n + 1)
dist[A] = 0
pq = []
heapq.heappush(pq, (0, A))
while pq:
    min_dist, min_index = heapq.heappop(pq)

    if min_dist > dist[min_index]:
        continue 
    for target_index, target_dist in graph[min_index]:
        new_dist = min_dist + target_dist
        if dist[target_index] > new_dist:
            dist[target_index] = new_dist
            heapq.heappush(pq, (new_dist, target_index))
print(dist[B])



