from sys import stdin

input = stdin.readline


def dfs(s, e, d):
    global dist

    if s == e:
        dist = d
        return

    for nxt_n, nxt_d in vertex[s]:
        if visited[nxt_n]:
            visited[nxt_n] = False  # 방문 처리
            dfs(nxt_n, e, d + nxt_d)


n, m = map(int, input().split())  # n: 정점의 개수, m: 정점 쌍의 개수

vertex = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    v1, v2, w = map(int, input().split())  # v1 <-> v2: 가중치 w
    vertex[v1].append((v2, w))
    vertex[v2].append((v1, w))

for _ in range(m):
    s, e = map(int, input().split())
    visited = [True] * (n + 1)
    visited[s] = False  # 출발 지점 방문 처리
    dist = 0
    dfs(s, e, 0)

    print(dist)
