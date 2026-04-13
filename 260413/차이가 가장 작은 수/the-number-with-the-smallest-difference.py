from sortedcontainers import SortedSet

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
s = SortedSet()
answer = 1000
# Please write your code here.
for i in arr:
    s.add(i)
for x in s:
    idx = s.bisect_left(x + m)
    
    if idx < len(s):
        diff = s[idx] - x
        answer = min(answer, diff)

print(answer)