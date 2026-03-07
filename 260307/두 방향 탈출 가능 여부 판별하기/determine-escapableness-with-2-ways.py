n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]  # 이 줄 추가!
order = 0
cnt =0
answer = [[0] * m for _ in range(n)]   # answer도 선언 필요!
# Please write your code here.
def dfs(x,y):
    global order
    global cnt
    dxs,dys =[1,0],[0,1]

    answer[x][y] = order
    order +=1
    visited[x][y] = 1

    if x == n-1 and y == m-1:  # 목적지 도달 시
        cnt += 1
        visited[x][y] = 0      # 복원
        return
        
    for dx,dy in zip(dxs,dys):
        new_x, new_y = x+dx, y+ dy

        if can_go(new_x,new_y):
            if visited[new_y][new_x] == 1:
                return
            dfs(new_x,new_y)

def in_range(x,y):
    return 0 <= x and x<n and\
            0 <= y and y<m

def can_go(x,y):
    if not in_range(x,y):
        return False
    if visited[x][y] or grid[x][y] ==0:
        return False
    return True



dfs(0,0)
print(cnt)