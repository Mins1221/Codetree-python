n = int(input())
board =[]
for i in range(n):
    board.append(list(map(int,input().split())))

# Please write your code here.

bombs = []
for r in range(n):
    for c in range(n):
        if board[r][c] == 1
            bombs.append((r,c))
max_count =0

def find(idx):
    if idx == len(bombs):
        return max_count

    폭탄1 (상하 2칸)
    (r-2,c) (r-1,c) (r,c) (r+1,c) (r+2,c)
def bomb1(r,c):
    board[r-2][c] =1
    board[r-2][c] =1

폭탄2 (상하좌우 1칸)
    (r,c) (r-1,c) (r+1,c) (r,c-1) (r,c+1)

폭탄3 (대각선 1칸)
    (r,c) (r-1,c-1) (r-1,c+1) (r+1,c-1) (r+1,c+1)

    

find(0)
print(max_count)
