from collections import deque
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] *m for _ in range(n)]
q = deque()
cnt = 0
step = [[-1] * m for _ in range(n)] 

# Please write your code here.
def bfs():
    global cnt
    dxs,dys = [1,-1,0,0], [0,0,1,-1]

    while q:
        x,y = q.popleft()

        for dx,dy in zip(dxs,dys):
            new_x, new_y = x + dx, y + dy
            if can_go(new_x,new_y):
               push(new_x,new_y,step[x][y]+1)
def in_range(x,y):
    return 0 <= x < n and \
           0 <= y < m

def can_go(x,y):
    if not in_range(x,y):
        return False
    if not visited[x][y] and a[x][y] == 1:
        return True
    return False

def push(x,y,s):
    step[x][y] = s
    visited[x][y] = True
    q.append((x,y))

push(0,0,0)
bfs()
if a[0][0] == 1:  # 시작점 체크 추가
    push(0, 0, 0)
print(step[n-1][m-1])