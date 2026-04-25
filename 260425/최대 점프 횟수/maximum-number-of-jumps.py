n = int(input())
arr = list(map(int, input().split()))

dp = [0] * n

dp[0] = 1  # 시작점은 항상 도달 가능

for i in range(1, n):
    for j in range(i):
        if dp[j] > 0 and j + arr[j] >= i:  # j가 0에서 도달 가능할 때만
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp) - 1) 