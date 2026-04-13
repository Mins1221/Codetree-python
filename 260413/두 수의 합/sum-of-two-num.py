n, k = map(int, input().split())
arr = list(map(int, input().split()))

count = 0
d = dict()
for val in arr:
    if k - val in d:
        count += d[k - val]  # True 대신 몇 번 등장했는지만큼 더하기
    if val in d:
        d[val] += 1
    else:
        d[val] = 1

print(count)