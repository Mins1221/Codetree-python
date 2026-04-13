n, k = map(int, input().split())
arr = list(map(int, input().split()))

count = 0
d = dict()
for val in arr:
    if k - val in d:
        count +=1
    d[val] = True

print(count)