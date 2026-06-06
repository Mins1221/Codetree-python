from bisect import bisect_left, bisect_right
n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [int(input()) for _ in range(m)]


for qu in queries:
    print(bisect_right(arr,qu)-bisect_left(arr,qu))
    