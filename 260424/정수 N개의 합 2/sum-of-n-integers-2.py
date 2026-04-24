n, k = map(int, input().split())
arr = list(map(int, input().split()))
prefix_sum = [0] *n
# Please write your code here.
prefix_sum[0] = arr[0]
for i in range(n):
    prefix_sum[i] = prefix_sum[i-1] + arr[i]

max_val = 0
for i in range(n):
    max_val =max(max_val,prefix_sum[i] - prefix_sum[i-k])

print(max_val)