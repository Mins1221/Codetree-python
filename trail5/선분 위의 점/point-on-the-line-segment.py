from bisect import bisect_right, bisect_left
n,m = map(int,input().split())
arr = list(int(input().split()))
line = [int(input().split()) for _ in range(m)]

for s,e in line:
    print(bisect_right(arr,e) - bisect_left(arr,s))