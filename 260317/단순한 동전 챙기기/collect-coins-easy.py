from collections import deque
n = int(input())
grid = [list(input()) for _ in range(n)]

# Please write your code here.
pos= {}
for r in range(n):
    for c in range(n):
        if grid[r][c] == 'S':
            pos['S'] = (r,c)
        elif grid[r][c] =='E':
            pos['E'] = (r,c)
        elif grid[r][c].isdigit():
            pos[int(grid[r][c])] = (r,c)

coins = sorted([k for k in pos if isinstance(k,int)])

def bfs(start,end):
    if start == end :
        return 0
    sr, sc = start
    er, ec = end
    queue = deque([(sr,sc,0)])
    visited = [[False]*n for _ in range(n)]
    visited[sr][sc] = True

    while queue :
        r,c, dist = queue.popleft()
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr,nc = r+dr,c+dc
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                if (nr,nc) == (er,ec):
                    return dist + 1
                visited[nr][nc] = True
                queue.append((nr,nc,dist +1))

    return -1

result = -1

for i in range(len(coins)):
    for j in range(i+1,len(coins)):
        for k in range(j+1,len(coins)):
            a,b,c = coins[i],coins[j],coins[k]
            d1 = bfs(pos['S'],pos[a])
            d2 = bfs(pos[a],pos[b])
            d3 = bfs(pos[b],pos[c])
            d4 = bfs(pos[c],pos['E'])

            if -1 in (d1,d2,d3,d4):
                continue
            total = d1 + d2 + d3 + d4
            if result == -1 or total < result:
                result = total

print(result)