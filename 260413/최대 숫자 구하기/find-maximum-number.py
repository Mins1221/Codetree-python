from sortedcontainers import SortedSet
n, m = map(int, input().split())
queries = list(map(int, input().split()))
s = SortedSet()
# Please write your code here.
for i in range(1,m+1):
    s.add(i)

for elem in queries:
    s.remove(elem)
    print(s[-1])