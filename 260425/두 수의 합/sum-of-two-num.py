n, k = map(int, input().split())
arr = list(map(int, input().split()))
count = 0
d = dict()
for elem in arr:
    if k-elem in d:
        count += d[k - elem]
    if elem in d:
        d[elem] +=1
    else:
        d[elem] =1
    
print(count)