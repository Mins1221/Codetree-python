from collections import deque
MOD = 1000000007
n, m = tuple(map(int, input().split()))
edges = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
needs = [
    [0] * (n + 1)
    for _ in range(n + 1)
]
q = deque()
for _ in range(m):
    x, y, z = tuple(map(int, input().split()))

    edges[y].append((x, z))
    indegree[x] += 1 
for i in range(1, n + 1):
    if not indegree[i]:
        q.append(i)
        needs[i][i] = 1
while q:
    x = q.popleft()
    for y, num in edges[x]:
        for j in range(1, n + 1):
            needs[y][j] += num * needs[x][j]
        indegree[y] -= 1
        if not indegree[y]:
            q.append(y)
for i in range(1, n + 1):
    if needs[n][i]:
        print(i, needs[n][i])
