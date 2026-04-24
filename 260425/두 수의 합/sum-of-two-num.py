n, k = map(int, input().split())
arr = list(map(int, input().split()))
count = 0
d = dict()
for i,elem in enumerate(arr):
    d[elem] = i+1

    if k-elem in d:
        count +=1
    
print(count)