from sortedcontainers import SortedSet
import sys
n = int(input())
queries = list(map(int, input().split()))
s = SortedSet()
# Please write your code here.
s.add(0)
ans = sys.maxsize
for i in queries:
    idx = s.bisect_right(i)
    if idx != len(s):
        ans = min(ans,s[idx]-i)
    idx -=1
    ans = min(ans,i-s[idx])
    s.add(i)
    print(ans)