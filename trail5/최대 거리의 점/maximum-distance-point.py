import sys
n, m = map(int, input().split())
points = [int(input()) for _ in range(n)]
input = sys.stdin.readline

def can_place(points,m,d):
    count = 1
    last = points[0]
    for p in points[1:]:
        if p - last >= d:
            count +=1
            last = p
            if count >= m:
                return True
    return False

points.sort()

low,high = 1,points[-1] - points[0]
ans = 0

while low <= high:
    mid = (low+high) //2
    if can_place(points,m,mid):
        ans =mid
        low = mid +1

    else:
        high = mid -1

print(ans)

