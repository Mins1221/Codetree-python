n, m = map(int, input().split())
segments = [tuple(map(int, input().split())) for _ in range(m)]

INT_MUM = 10**18 +1
def clac(dist):
    cnt =0
    left = -INT_MUM
    for s,e in segments:
        while left + dist <= e:
            cnt +=1
            left = max(s,left+dist)
            if cnt >= n:
                break
    return cnt >= n
segments.sort()
left = 1
right = INT_MUM
ans = 0
while left <= right :
    mid = (left + right) //2
    if clac(mid):
        left = mid +1
        ans = mid
    else:
        right = mid -1
print(ans)

