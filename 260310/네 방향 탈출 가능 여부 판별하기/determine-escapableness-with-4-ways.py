from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
order = 0 
visited = [[0] * m for _ in range(n)]
answer = [[0] * m for _ in range(n)]
q =deque()
cnt = 0
# Please write your code here.
def bfs():
    global cnt
    dxs = [1,0]

    dys = [0,1]

    while q:
        x,y = q.popleft()


        for dx, dy in zip(dxs,dys):
            new_x, new_y = x +dx, y+ dy

            if can_go(new_x, new_y):
                push(new_x,new_y)



def in_range(x,y):
    return 0 <= x < n and \
           0 <= y < m
def can_go(x,y):
    if not in_range(x,y):
        return False
    if visited[x][y] == 1 or grid[x][y] == 0:
        return False
    return True

def push(x,y):
    global order

    answer[x][y] = order
    order +=1
    visited[x][y] = True
    q.append((x,y))

push(0,0)
bfs()

print(cnt)


