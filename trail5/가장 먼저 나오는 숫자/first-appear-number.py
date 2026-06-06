n,m = map(int,input().split())
arr = list(map(int,input().split()))
x = list(map(int,input().split()))
import bisect
for num in x:
    i = bisect.bisect_left(arr,num)
    if i < n and arr[i] == num:
        print(i+1)
    else:
        print(-1)

