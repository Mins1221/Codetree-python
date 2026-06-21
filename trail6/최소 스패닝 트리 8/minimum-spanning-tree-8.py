import heapq
import sys
input = sys.stdin.readline

def prim():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((w, v))   # (가중치, 도착정점)
        graph[v].append((w, u))   # 무방향이므로 양쪽 다

    visited = [False] * (n + 1)
    heap = [(0, 1)]               # (간선 가중치, 시작 정점) — 1번부터 시작
    total = 0
    count = 0

    while heap and count < n:
        w, node = heapq.heappop(heap)
        if visited[node]:          # 이미 트리에 들어온 정점이면 스킵
            continue
        visited[node] = True
        total += w
        count += 1
        for nw, nxt in graph[node]:
            if not visited[nxt]:
                heapq.heappush(heap, (nw, nxt))

    return total

print(prim())