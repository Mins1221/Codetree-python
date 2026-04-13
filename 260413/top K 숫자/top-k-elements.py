from sortedcontainers import SortedSet
n, k = map(int, input().split())
arr = list(map(int, input().split()))
s = SortedSet()
new = SortedSet()
# Please write your code here.
for i in arr:
    s.add(i)
    new = sorted(s,reverse= True)
for j in range(min(k, len(new))):
    print(new[j], end=" ")