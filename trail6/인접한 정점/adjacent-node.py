import sys
sys.setrecursionlimit(10000)
n = int(input())
edges = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
a = [0] + list(map(int, input().split()))
dp = [[0, 0] for _ in range(n + 1)]
for _ in range(n - 1):
    x, y = tuple(map(int, input().split()))
    edges[x].append(y)
    edges[y].append(x)
def dfs(x):
    dp[x][1] = a[x]
    for y in edges[x]:
        if visited[y]: 
            continue
        visited[y] = True
        dfs(y)
        dp[x][1] += dp[y][0]
        dp[x][0] += max(dp[y][0], dp[y][1])
visited[1] = True
dfs(1)
print(max(dp[1][0], dp[1][1]))
