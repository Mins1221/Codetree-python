
arr = list(map(str,input()))
n = len(arr)
count = {}
ans = 0
j = -1
for i in range(n):
    while j + 1  <  n and count.get(arr[j+1], 0) != 1:
        count[arr[j+1]] = count.get(arr[j+1], 0) + 1
        j+=1

    ans = max(ans,j-i+1)
    count[arr[i]] -=1

print(ans)
