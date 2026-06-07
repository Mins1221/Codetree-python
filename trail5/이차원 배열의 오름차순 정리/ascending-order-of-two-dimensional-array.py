n = int(input())
k = int(input())

high = n*n
ans = n* n
low = 1
while low <= high :
    mid = (high +low) // 2
    val = 0
    for i in range(1,n+1):
        val +=min(n,mid // i)

    if val >= k:
        high = mid  -1
        ans = min(ans,mid)
    else:
        low = mid +1

print(ans)