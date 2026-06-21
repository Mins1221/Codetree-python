from collections import deque
n,m1,m2 = map(int,input().split())
edges = [[] for _ in range(n+1)]
indegree = [0] *(n+1)
q = deque()
for i in range(m1):
    x,y = tuple(map(int,input().split()))
    edges[x].append(y)
    indegree[y] +=1
for i in range(1,n+1):
    if not indegree[i]:
        q.append(i)
for i in range(m2):
    x,y = tuple(map(int,input().split()))
count = 0
while q:
    x = q.popleft()
    count +=1
    for y in edges[x]:
        indegree[y] -=1
        if not indegree[y]:
            q.append(y)
if count == n:
    print("Yes")
else:
    print("No")