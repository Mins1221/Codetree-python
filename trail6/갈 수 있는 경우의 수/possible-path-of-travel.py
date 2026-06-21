from collections import deque
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
graph = [[] for _ in range(n+1)]
q = deque()
indegree = [0] * (n + 1)
MOD = 1000000007
for x,y in edges:
    graph[x].append(y)
    indegree[y]+=1
for i in range(1 , n+1):
    if indegree[i] ==0:
        q.append(i)
dp = [0] * (n + 1)
dp[1] =1
while q:
    cnt = q.popleft()
    for nxt in graph[cnt]:
        dp[nxt] = (dp[nxt]+dp[cnt]) % MOD
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            q.append(nxt)
print(dp[n])

    
        