n, m = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] =1
    graph[b][a] =1
    


visited = [False] * (n+1)
vertex_cnt = 0

# Please write your code here.
def dfs(vertex):
    global vertex_cnt
    for curr_v in range(1,n+1):
        if graph[vertex][curr_v] and not visited[curr_v]:
            vertex_cnt +=1
            visited[curr_v] = True
            dfs(curr_v)

visited[1] = True
dfs(1)
print(vertex_cnt)