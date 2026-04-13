from sortedcontainers import SortedSet
import sys
n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
s = SortedSet()
answer = sys.maxsize
max_answer = 0 
# Please write your code here.
for i in arr:
    s.add(i)
for x in s:
    idx = s.bisect_left(x + m)
    
    if idx < len(s):
        diff = s[idx] - x
        answer = min(answer, diff)
    else :
        if answer == sys.maxsize:
            answer = -1
        max_answer = max(-1,answer)
print(max_answer)

