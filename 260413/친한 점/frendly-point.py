from sortedcontainers import SortedSet
n, m = map(int, input().split())
s = SortedSet()
# Store points as list of tuples
points = [tuple(map(int, input().split())) for _ in range(n)]

# Store queries as list of tuples
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
for k in points:
    s.add(k)

for i in queries:
    if s.bisect_left(i) == len(s):
        print("-1 -1")
    else:
        print(*s[s.bisect_left(i)])