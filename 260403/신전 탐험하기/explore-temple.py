import sys
INT_MIN = -sys.maxsize

n = int(input())
l, m, r = [], [], []
for _ in range(n):
    left, mid, right = map(int, input().split())
    l.append(left)
    m.append(mid)
    r.append(right)

# dp[i][1~3] = i층에서 왼/중/오 선택시 최대값
dp = [[0]*4 for _ in range(n+1)]

for i in range(1, n+1):
    dp[i][1] = INT_MIN
    dp[i][2] = INT_MIN
    dp[i][3] = INT_MIN

# 1층 초기화
dp[1][1] = l[0]
dp[1][2] = m[0]
dp[1][3] = r[0]

# 점화식 (0-based 리스트이므로 a[i] → l[i-1], m[i-1], r[i-1])
room = [None, l, m, r]  # 1-based로 접근하기 위한 매핑

for i in range(2, n+1):
    for j in range(1, 4):
        for k in range(1, 4):
            if j != k:
                dp[i][j] = max(dp[i][j], dp[i-1][k] + room[j][i-1])

ans = 0
for j in range(1, 4):
    ans = max(ans, dp[n][j])

print(ans)