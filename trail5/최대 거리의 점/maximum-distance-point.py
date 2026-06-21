import sys
input = sys.stdin.readline
n,m = map(int,input().split())
point = [int(input()) for _ in range(n)]
def calc(point,m,d):
    last = point[0]
    count = 1
    for p in point[1:]:
        if p - last >= d:
            last = p
            count +=1
            if count >= m:
                return True
    return False
point.sort()
low,high = 1, point[-1] - point[0]
ans = 0
while low <= high :
    mid = (low + high) // 2
    if calc(point,m,mid):
        ans =mid
        low = mid +1
    else:
        high = mid -1
print(ans)