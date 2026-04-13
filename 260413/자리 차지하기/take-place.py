from sortedcontainers import SortedSet
n, m = map(int, input().split())
a = list(map(int, input().split()))
s = SortedSet()
# Please write your code here.
count = 0
for i in range(1,m+1):
    s.add(i)

for x in a:
    idx = s.bisect_right(x) - 1

    if idx< 0:
        break

    s.remove(s[idx])
    count +=1
print(count)
