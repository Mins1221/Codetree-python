n, k = map(int, input().split())
s = input()
a = []
for c in s:
    if c == 'L':
        a.append(0) # 왼쪽=0
    else:
        a.append(1)  # 오른쪽=1
INF = float('-inf')
dp = [[INF] * (k + 2) for _ in range(n + 1)]
dp[0][0] = 0

for i in range(n):
    for j in range(k + 1):
        if dp[i][j] == INF:
            continue
        # 이동 안 함
        pos = j % 2
        gain = 1 if a[i] == pos else 0
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + gain)

        # 이동 함
        if j + 1 <= k:
            pos2 = (j + 1) % 2
            gain2 = 1 if a[i] == pos2 else 0
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + gain2)

print(max(dp[n][:k + 1]))