n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
cnt =0

# Please write your code here.
def dfs(x,y):
    global cnt
 
    dxs,dys = [1,-1,0,0], [0,0,1,-1]

    for dx, dy in zip(dxs,dys):
        new_x = x + dx
        new_y = y + dy
        if can_go(new_x,new_y):
            visited[new_x][new_y] = 1
            cnt +=1
            dfs(new_x,new_y)


def in_range(x,y):
    return 0 <= x  and x < n \
            and 0 <= y  and y < n

def can_go(x,y):
    if not in_range(x,y):
        return False
    if visited[x][y] == 0 and grid[x][y] == 1:
        return True
    return False

villages = []
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and grid[i][j] == 1:
            cnt =1
            visited[i][j] = 1
            dfs(i,j)
            villages.append(cnt)

print(len(villages))
print(*sorted(villages),sep = '\n')