from sortedcontainers import SortedDict
n = int(input())
words = [input() for _ in range(n)]
d = SortedDict()
# Please write your code here.

for elem in words:
    if elem not in d:
        d[elem] = 1
    else:
        d[elem] +=1

for key, value in d.items():
    print(key,value)