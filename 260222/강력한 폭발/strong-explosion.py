n = int(input())
board =[]
for i in range(n):
    board.append(list(map(int,input().split())))

# Please write your code here.

bombs = []
for r in range(n):
    for c in range(n):
        if board[r][c] == 1:
            bombs.append((r,c))





def find(idx):
    if idx == len(bombs):
        global max_count
        current = 0
        for r in range(n):
            for c in range(n):
                if board[r][c] == 1:
                    current += 1
        max_count = max(max_count, current)
        return 
    r, c = bombs[idx]
    
    for i in range(1, 4):
        changed = []
        if i == 1:
            bomb1(r, c, changed)
        elif i == 2:
            bomb2(r, c, changed)
        elif i == 3:
            bomb3(r, c, changed)
        
        find(idx + 1)
        
        # 되돌리기
        for r2, c2 in changed:
            board[r2][c2] = 0

def bomb1(r, c, changed):
    for nr in [r-2, r-1, r, r+1, r+2]:
        if 0 <= nr < n:        # 범위 체크
            if board[nr][c] == 0:  # 원래 0인 칸만
                board[nr][c] = 1
                changed.append((nr, c))  # 기록

def bomb2(r, c, changed):
    for nr, nc in [(r,c),(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
        if 0 <= nr < n and 0 <= nc < n:
            if board[nr][nc] == 0:
                board[nr][nc] = 1
                changed.append((nr, nc))


def bomb3(r, c, changed):
    for nr, nc in [(r,c),(r-1,c-1),(r-1,c+1),(r+1,c-1),(r+1,c+1)]:
        if 0 <= nr < n and 0 <= nc < n:
            if board[nr][nc] == 0:
                board[nr][nc] = 1
                changed.append((nr, nc))


    
max_count =0
find(0)
print(max_count)
