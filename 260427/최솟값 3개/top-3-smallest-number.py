from sortedcontainers import SortedSet
n = int(input())

arr = list(map(int, input().split()))
s= SortedSet()

for i in arr:
    s.add(i)
    if len(s) < 3:
        print(-1)
    else:
       sum = s[0]*s[1]*s[2]
       print(sum)