from sortedcontainers import SortedSet

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
s = SortedSet()
answer = 1000
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
        if answer == 1000:
            answer = -1
        max_answer = max(-1,answer)
print(max_answer)

