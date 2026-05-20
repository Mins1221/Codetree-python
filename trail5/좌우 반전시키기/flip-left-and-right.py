n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

ans = 0
for i in range(1,n):
    if i == n-1 and arr[i-1] == 0:
        arr[i-1] = 1
        arr[i] = 1^arr[i]
        ans+=1
        break
    if arr[i-1] == 0:
        arr[i-1] = 1
        arr[i] = 1^arr[i]
        arr[i+1] = 1^arr[i+1]
        ans+=1


if 0 in arr:
    print(-1)
else:
    print(ans)
