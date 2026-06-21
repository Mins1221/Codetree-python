n,m = map(int,input().split())
segment = [tuple(map(int,input().split())) for _ in range(m)]
MAM_MUM = 10**18 +1
def calc(dist):
    left = -MAM_MUM
    cnt = 0
    for s,e in segment:
        while left + dist <= e:
            left = max(s,left+dist)
            cnt +=1
        if cnt >= n:
            break
    return cnt >= n
segment.sort()
left =1
right = MAM_MUM
ans = 0
while left <= right:
    mid = (left+right) //2
    if calc(mid):
        left = mid +1
        ans = mid
    else:
        right = mid-1

print(ans)
