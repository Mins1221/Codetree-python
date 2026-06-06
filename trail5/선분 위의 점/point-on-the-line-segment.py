import bisect
n,m = map(int,input().split())
arr = map(int,input().split())
lines = [list(map(int,input().split())) for _ in range(m)]

arr = sorted(arr)
for s,e in lines:
    l = bisect.bisect_left(arr,s)
    r = bisect.bisect_right(arr,e)
    print(r-l)