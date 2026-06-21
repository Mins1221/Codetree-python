n,m = map(int,input().split())
arr = [int(input()) for _ in range(n)]
l =1
r =n
ans =0
while l <= r:
    mid = (l+r) // 2
    count = sum(x // mid for x in arr)

    if count >= m:
        ans = mid
        l = mid +1
    else:
        r = mid -1
print(ans)
