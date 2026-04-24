def solve():
    N, M, K = map(int, input().split())
    grid = []
    for _ in range(N):
        grid.append(input().strip())

    # a, b, c 각각 2D prefix sum
    prefix = {ch: [[0]*(M+1) for _ in range(N+1)] for ch in 'abc'}

    for i in range(1, N+1):
        for j in range(1, M+1):
            for ch in 'abc':
                val = 1 if grid[i-1][j-1] == ch else 0
                prefix[ch][i][j] = (prefix[ch][i-1][j]
                                  + prefix[ch][i][j-1]
                                  - prefix[ch][i-1][j-1]
                                  + val)

    def query(ch, r1, c1, r2, c2):
        return (prefix[ch][r2][c2]
              - prefix[ch][r1-1][c2]
              - prefix[ch][r2][c1-1]
              + prefix[ch][r1-1][c1-1])

    for _ in range(K):
        r1, c1, r2, c2 = map(int, input().split())
        print(query('a',r1,c1,r2,c2),
              query('b',r1,c1,r2,c2),
              query('c',r1,c1,r2,c2))

solve()