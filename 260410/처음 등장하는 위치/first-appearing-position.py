from sortedcontainers import SortedDict
n = int(input())
arr = list(map(int, input().split()))
d = SortedDict()
# Please write your code here.
for i,elem in enumerate(arr):
    if elem not in d:
      d[elem] = i+1
    
    
for k,v in d.items():
    print(k,v)
        