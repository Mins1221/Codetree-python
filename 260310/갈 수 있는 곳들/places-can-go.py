from collections import deque
n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
points=[]
for _ in range(k):
        x,y = map(int,input().split())
        points.append((x-1,y-1))

# Please write your code here.
visited = [[0]*n for _ in range(n)]
cnt =0
q = deque()
def bfs():
    global cnt

    dxs, dys = [1,-1,0,0], [0,0,1,-1]


    while q:
        x,y = q.popleft()
        for dx,dy in zip(dxs,dys):
            new_x, new_y = x +dx, y + dy

            if can_go(new_x,new_y):
                push(new_x,new_y)
            
def in_range(x,y):
    return 0 <= x < n and \
           0 <= y < n
        
def can_go(x,y):
    if not in_range(x,y):
        return False
    if visited[x][y] == 0 and grid[x][y] == 0 :
        return True
    return False

def push(x,y):
    global cnt

    visited[x][y] = True
    q.append((x,y))
    cnt +=1

for x,y in points:
    if can_go(x,y):
        push(x,y)

bfs()
print(cnt)

