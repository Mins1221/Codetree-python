n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
visited = [False] * n
max_val =0

def max_num(col, curr_sum):
    global max_val
    if col == n:
        max_val = max(max_val,curr_sum)
        return

    for row in range(n):
        if visited[row]:
            continue

        visited[row] = True
        max_num(col+1,curr_sum + grid[row][col])
        visited[row] = False
max_num(0,0)
print(max_val)
            
