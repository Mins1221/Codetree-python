from sortedcontainers import SortedSet
n, m = map(int, input().split())
nums = list(map(int, input().split()))
s = SortedSet()
# Please write your code here.
for l in range(n+1):
    s.add(l)

 
for k in nums:
    s.remove(k)
    num = 1
    max_num =1
    for i in range(len(s)-1):
        if s[i+1] -s[i] ==1:
            num +=1
            max_num = max(max_num,num)
        else:
            num =1
    print(max_num)
