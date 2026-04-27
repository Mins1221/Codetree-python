n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [False] *(n+1)
max_val = 0

def choose(col,curr_sum):
    global max_val
    if col ==n:
        max_val = max(max_val,curr_sum)
        return
    for row in range(n):
        if visited[row] :
            continue

        visited[row] = True
        choose(col+1,curr_sum + grid[row][col])
        visited[row] = False

choose(0,0)
print(max_val)
