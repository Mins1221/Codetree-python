n, k = map(int, input().split())
arr = list(map(int, input().split()))
count = 0
d = dict()
for i,elem in enumerate(arr):
    if k-elem in d:
        count +=1
    d[elem] = i+1
    
print(count)