n, m = map(int, input().split())
segments = [tuple(map(int, input().split())) for _ in range(m)]
segments.sort()
# Please write your code here.
def calc_how_many(dist):
    cnt=0
    left=-dist
    for s, e in segments:
        left=max(left+dist, s)
        if left<=end:
            cnt+=(e-left)//dist
            cnt+=1
        left+=(e-left)//dist*dist
    return cnt

left=1
right=10**18+1
ans=0

while left<=right:
    mid=(left+right)//2
    if calc_how_many(mid)>=n:
        ans=max(ans, mid)
        left=mid+1
    else:
        right=mid-1
print(ans)


