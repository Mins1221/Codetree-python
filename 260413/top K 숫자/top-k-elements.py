from sortedcontainers import SortedSet
n, k = map(int, input().split())
arr = list(map(int, input().split()))
s = SortedSet()

# Please write your code here.
for i in arr:
    s.add(i)
for j in range(1,1+k):
    print(s[-j],end=" ")   