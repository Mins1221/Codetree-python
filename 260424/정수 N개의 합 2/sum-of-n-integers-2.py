n, k = map(int, input().split())
arr = list(map(int, input().split()))
prefix_sum = [0] * (n+1)


prefix_sum[0] = arr[0]
for i in range(1,n):
    prefix_sum[i] = prefix_sum[i-1] + arr[i]

max_sum = 0
for i in range(len(arr) - k + 1):
    current = prefix_sum[i+k] - prefix_sum[i]
    if current > max_sum:
        max_sum = current

print(max_sum) 
