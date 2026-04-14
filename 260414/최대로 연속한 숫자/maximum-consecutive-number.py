from sortedcontainers import SortedSet,SortedList
n, m = map(int, input().split())
nums = list(map(int, input().split()))
s = SortedSet()
# Please write your code here.
for l in range(n+1):
    s.add(l)
runs = SortedList([n+1])
 
for k in nums:
    idx = s.index(k)
    s.remove(k)
    left_idx = idx - 1
    left_count = 0
    while left_idx >= 0 and s[left_idx] == k - 1 - left_count:
        left_count += 1
        left_idx -= 1

    right_idx = idx 
    right_count = 0
    while right_idx < len(s) and s[right_idx] == k+1 +right_count: 
        right_count += 1
        right_idx += 1 # 초기엔 전체가 연속

    runs.remove(left_count + right_count + 1)
    if left_count > 0: runs.add(left_count)
    if right_count > 0: runs.add(right_count)
    
    print(runs[-1])