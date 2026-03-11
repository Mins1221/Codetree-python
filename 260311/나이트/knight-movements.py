from collections import deque
n = int(input())
r1, c1, r2, c2 = map(int, input().split())
q =deque()
cnt = 0
step = [[-1] * (n+1) for _ in range(n+1)] 
visited = [[0] *(n+1) for _ in range(n+1)]
# Please write your code here.
def bfs():
    global cnt
    dxs = [-2,-2,-1,-1,1,1,2,2]
    dys = [-1,1,-2,2,-2,2,-1,1]
    
    while q:

        x,y = q.popleft()

        if (x,y) == (r2,c2) :
            return

        for dx,dy in zip(dxs,dys):
            new_x, new_y = x + dx, y + dy
            if can_go(new_x,new_y):
                push(new_x,new_y, step[x][y] +1)

def in_range(x,y):
    return 1 <= x <= n and \
           1 <= y <= n

def can_go(x,y):
    if not in_range(x,y):
        return False
    if not visited[x][y] == 1  :
        return True
    return False

def push(x,y,s):
    global cnt
    step[x][y] = s
    visited[x][y] = True
    q.append((x,y))

push(r1,c1,0)
bfs()

print(step[r2][c2])
