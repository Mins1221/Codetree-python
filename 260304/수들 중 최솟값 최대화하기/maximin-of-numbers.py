n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
visited = [False] *n
min_val = 0

def solve(col):
    global min_val
    if col == n :
        min_val = max(col,min_val)
        return

    for row in range(n):
        if visited[row] : 
            continue
        
        visited[row] = True
        solve(col+1)
        visited[row] = False

solve(0)
print(min_val)