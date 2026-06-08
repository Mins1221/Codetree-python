from collections import deque
n, m1, m2 = tuple(map(int, input().split()))
edges = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
visited = [False] * (n + 1)
q = deque()
for _ in range(m1):
    x, y = tuple(map(int, input().split()))

    edges[x].append(y) 
    indegree[y] += 1
for _ in range(m2):
    a, b = tuple(map(int, input().split()))
for i in range(1, n + 1):
    if not indegree[i]:
        q.append(i)
while q:
    x = q.popleft()

    visited[x] = True
    for y in edges[x]:
        indegree[y] -= 1
        if not indegree[y]:
            q.append(y)
is_cycle = False
for i in range(1, n + 1):
    if not visited[i]: 
        is_cycle = True
if is_cycle:
    print("No")
else:
    print("Yes")
