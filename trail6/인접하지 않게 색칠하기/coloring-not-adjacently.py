import sys
sys.setrecursionlimit(100000)
n = int(input())
edges = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
for _ in range(n - 1):
    x, y = tuple(map(int, input().split()))
    edges[x].append(y)
    edges[y].append(x)
a = [0] * (n + 1)
for i in range(1, n + 1):
    a[i] = int(input())
k = int(input())
dp = [[[0, 0] for _ in range(k + 1)] for _ in range(n + 1)]
ans = 0
def dfs(x):
    dp[x][1][1] = a[x]
    dp[x][0][0] = 0
    for y in edges[x]:
        if visited[y]: 
            continue
        visited[y] = True
        dfs(y)
        for i in range(k, 0, -1):
            for j in range(1, i + 1):
                dp[x][i][1] = max(dp[x][i][1], dp[x][i - j][1] + dp[y][j][0])
        for i in range(k, -1, -1):
            for j in range(i + 1):
                dp[x][i][0] = max(dp[x][i][0], 
                                  dp[x][i - j][0] + 
                                  max(dp[y][j][0], dp[y][j][1]))
dfs(1)

for i in range(1, k + 1):
    ans = max(ans, dp[1][i][0])
    ans = max(ans, dp[1][i][1])

print(ans)
