import heapq

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
A, B = map(int, input().split())

graph = [[] for _ in range(n+1)]

for x, y, z in edges:
    graph[x].append((y, z))
    graph[y].append((x, z))

def dijkstra(start):
    dist = [float('inf')] * (n+1)
    dist[A] = 0

    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        cost, node = heapq.heappop(pq)

        if dist[node] < cost:
            continue

        for next_node, weight in graph[node]:
            if dist[next_node] >= cost + weight:
                dist[next_node] = cost + weight
                heapq.heappush(pq, (dist[next_node], next_node))
    return dist[B]


print(dijkstra(A))

