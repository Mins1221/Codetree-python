from bisect import bisect_right,bisect_left
n,m = map(int,input().split())
arr = list(map(int,input().split()))
queries = [int(input()) for _ in range(m)]
for i in queries:
    print(bisect_right(arr,i) - bisect_left(arr,i))