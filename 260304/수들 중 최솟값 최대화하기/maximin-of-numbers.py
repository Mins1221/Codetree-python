n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
visited = [False] *n
min_val = 0

def solve(col,curr_min):
    global min_val
    if col == n :
        min_val = max(min_val,curr_min)
        return

    for row in range(n):
        if visited[row] : 
            continue
        
        visited[row] = True
        solve(col+1, min(curr_min, grid[row][col]))
        visited[row] = False

solve(0,1370345)
print(min_val)