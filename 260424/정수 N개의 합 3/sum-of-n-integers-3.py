n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
prefix_sum = [[0]*(n+1) for _ in range(n+1)]
# Please write your code here.
for i in range(1,n+1):
    for j in range(1,n+1):
        prefix_sum[i][j] = prefix_sum[i-1][j] + \
                           prefix_sum[i][j-1] - \
                           prefix_sum[i-1][j-1] + \
                           arr[i-1][j-1] 
max_sum = 0
for i in range(k, n + 1):
    for j in range(k, n + 1):
        # (i-k, j-k) ~ (i, j) 구간의 K×K 합
        current = prefix_sum[i][j] \
                - prefix_sum[i-k][j] \
                - prefix_sum[i][j-k] \
                + prefix_sum[i-k][j-k]
        if current > max_sum:
            max_sum = current  # ← 방향 주의!

print(max_sum)