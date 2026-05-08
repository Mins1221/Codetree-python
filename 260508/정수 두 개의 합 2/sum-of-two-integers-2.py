n, k = map(int, input().split())
arr = [0] + [int(input()) for _ in range(n)]
arr.sort()
count = 0
left =1
right = n

for i in range(1,n+1):
    while left < right :
        if arr[left] + arr[right] <= k:
            count += right - left
            left +=1
        else :
            right -=1

print(count)