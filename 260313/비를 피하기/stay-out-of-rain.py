from collections import deque
n, h, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

people = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            people.append((i, j))
        
# Please write your code here.
def bfs():
    global cnt

    dxs = [-1,1,0,0]
    dys = [0,0,1,-1]

    while q:
        
        x,y = q.popleft()

        if grid[x][y] == 3:
            return step[x][y]

        for dx, dy in zip(dxs,dys):
            new_x = x + dx
            new_y = y + dy
                
            if can_go(new_x,new_y):
                push(new_x,new_y,step[x][y]+1)

    return -1


def in_range(x,y):
    return 0 <= x < n and \
           0 <= y < n 

def can_go(x,y):
    if not in_range(x,y):
        return False
    if not visited[x][y] and grid[x][y] != 1:
        return True
    return False

def push(x,y,s) :
    step[x][y] = s
    visited[x][y] = True
    q.append((x,y))

result_grid = [[0] * n for _ in range(n)]
for start_x, start_y in people: 
    visited = [[0] * n for _ in range(n)]
    step = [[-1] * n for _ in range(n)] 
    q = deque()
    q.append((start_x, start_y))
    visited[start_x][start_y] = 1
    step[start_x][start_y] = 0
    result_grid[start_x][start_y] = bfs()


for row in result_grid:
    print(*row)


