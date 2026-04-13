from sortedcontainers import SortedSet
n = int(input())
queries = list(map(int, input().split()))
s = SortedSet()
# Please write your code here.
s.add(0)
min_value = 1000
for i in queries:
    s.add(i)
    idx = s.index(i)
    if idx > 0:
        min_value = min(min_value, i - s[idx - 1])
        
    if idx +1 < len(s) :
        min_value = min(min_value,s[idx+1]- i)
    
    print(min_value)
