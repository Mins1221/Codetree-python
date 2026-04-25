n, m = map(int, input().split())  # n=목표금액, m=동전종류수
coins = list(map(int, input().split()))

dp = [-1] * (m + 1)  # -1 = 만들 수 없음
dp[0] = 0

for i in range(1, m + 1):      # i = 금액
    for coin in coins:          # 모든 동전 시도
        if i >= coin and dp[i - coin] != -1:
            dp[i] = max(dp[i], dp[i - coin] + 1)

print(dp[m]) 

