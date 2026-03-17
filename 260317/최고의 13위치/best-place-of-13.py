n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

max_cnt = 0
for i in range(n):
    for j in range(n - 2):  # j+2 must be < n, so j < n-2
        max_cnt = max(max_cnt, grid[i][j] +grid[i][j+1]+ grid[i][j+2])

print(max_cnt)

