n = int(input())
arr = [0] + list(map(int,input().split()))
count = [0] * (max(arr)+1)
j =0
ans =0
for i in range(1,n+1):
    while j+1 < n and count[arr[j+1]] != 1:
        count[arr[j+1]] += 1
        j+=1
        ans = max(ans,j-i+1)
        count[arr[i]] -= 1
print(ans)