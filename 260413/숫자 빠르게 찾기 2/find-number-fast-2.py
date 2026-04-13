from sortedcontainers import SortedSet
n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [int(input()) for _ in range(m)]
s = SortedSet()
# Please write your code here.
for k in arr:
    s.add(k)

for i in queries:

    if s.bisect_left(i) == len(s):
        print(-1)
    else:
        print(s[s.bisect_left(i)])

    
