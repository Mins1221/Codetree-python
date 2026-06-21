n, m = map(int, input().split())
segments = [tuple(map(int, input().split())) for _ in range(m)]
MAX_MUM = 10**18 +1
def calc(dist):
    left = -MAX_MUM
    cnt = 0
    for s,e in segments:
        while left + dist <= e:
            cnt +=1
            left = max(left+dist,s)
            if cnt >= n:
                break
    return cnt >= n
segments.sort()
left = 1
right = MAX_MUM
ans = 0
while left <= right:
    mid = (left + right) //2
    if calc(mid):
        left = mid +1
        ans =mid
    else:
        right = mid -1
print(ans)
