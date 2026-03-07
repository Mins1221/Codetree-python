n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]  
order = 0
cnt =0
answer = [[0] * m for _ in range(n)] 
# Please write your code here.
def dfs(x,y):
    global order
    global cnt
    dxs,dys = [1,0] , [0,1]

    answer[x][y] = order
    order += 1
    visited[x][y] = 1
    if x == n-1 and y == m-1:  # 목적지 도달 시
        cnt = 1
    
    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y+ dy

        if can_go(new_x, new_y):
            dfs(new_x, new_y)

#격자 내에 있는지 판단하는 함수
def in_range(x,y):
    return 0 <= x and x < n and \
           0 <= y and y < m

# new_x,new_y가 격자 안에 있고, 방문한 적 없고, 뱀이 없을 떄
def can_go(x,y):
    if not in_range(x,y):
        return False
    if visited[x][y] or grid[x][y] == 0:
        return False
    return True

dfs(0,0)
print(cnt)