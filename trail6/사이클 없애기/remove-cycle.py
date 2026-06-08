from collections import deque
n, m1, m2 = map(int, input().split())
edges = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
for i in range(m1):
    x,y = map(int, input().split())
    edges[x].append(y)
    indegree[y]+=1

for i in range(m2):
    x,y = map(int, input().split())
q = deque()
for i in range(1, n+1):
    if not indegree[i]:
        q.append(i)
ans = []
while q:
    now = q.popleft()
    ans.append(now)
    for x in edges[now]:
        indegree[x] -= 1
        if not indegree[x]:
            q.append(x)

print('Yes' if len(ans) == n else 'No')
