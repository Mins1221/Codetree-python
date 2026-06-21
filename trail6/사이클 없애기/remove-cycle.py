from collections import deque
n,m1, m2 = map(int,input().split())
indegree = [0] * (n+1)
edges = [[] for _ in range(n+1)]
q = deque()
for _ in range(m1):
    x,y = tuple(map(int,input().split()))
    edges[x].append(y)
    indegree[y] +=1
for i in range(1,n+1):
    if not indegree[i]:
        q.append(i)
for _ in range(m2):
    x,y = tuple(map(int,input().split()))
ans =[]
while q:
    now = q.popleft()
    ans.append(now)
    for x in edges[now]:
        indegree[x] -=1
        if not indegree[x]:
            q.append(x)
if len(ans) == n:
    print("Yes")
else:
    print("No")