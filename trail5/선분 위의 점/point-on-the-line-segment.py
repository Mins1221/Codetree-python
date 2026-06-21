from bisect import bisect_right, bisect_left
n,m = map(int,input().split())
arr = list(map(int,input().split()))
line = [list(map(int,input().split())) for _ in range(m)]
arr.sort()
for s,e in line:
    print(bisect_right(arr,e) - bisect_left(arr,s))