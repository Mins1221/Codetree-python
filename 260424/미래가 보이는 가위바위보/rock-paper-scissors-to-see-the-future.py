def solve():
    N = int(input())
    b_raw = [input().strip() for _ in range(N)]

    move_map = {'H': 0, 'S': 1, 'P': 2}  # 주먹, 가위, 보자기
    beats = {0: 1, 1: 2, 2: 0}           # 주먹→가위, 가위→보자기, 보자기→주먹

    b = [move_map[x] for x in b_raw]

    # L[i][j]: 1~i 구간, 패 j로만 낼 때 승리 수
    L = [[0] * 3 for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(3):
            win = 1 if beats[j] == b[i - 1] else 0
            L[i][j] = L[i - 1][j] + win

    # R[i][j]: i~N 구간, 패 j로만 낼 때 승리 수
    R = [[0] * 3 for _ in range(N + 2)]
    for i in range(N, 0, -1):
        for j in range(3):
            win = 1 if beats[j] == b[i - 1] else 0
            R[i][j] = R[i + 1][j] + win

    bestL = [max(L[k]) for k in range(N + 1)]
    bestR = [max(R[k]) for k in range(N + 2)]

    answer = max(bestL[k] + bestR[k + 1] for k in range(N + 1))
    print(answer)

solve()