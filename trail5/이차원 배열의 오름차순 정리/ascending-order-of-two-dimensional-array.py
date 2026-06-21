n = int(input())
k = int(input())
high = n*n
low = 1
ans = n*n
while low <= high:
    mid = (low+high) //2
    val =0
    for i in range(1,n+1):
        val += min(n,mid//i)
    if val >=k:
        ans = min(mid,ans)
        high = mid -1
    else:
        low = mid +1
print(ans)

