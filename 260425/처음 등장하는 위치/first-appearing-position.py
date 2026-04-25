from sortedcontainers import SortedDict
n = int(input())
arr = list(map(int, input().split()))

sd = SortedDict()
for i,elem in enumerate(arr):
    if elem not in sd:
        sd[elem] = i+1

for key,values in sd.items():
    print(key,values)


