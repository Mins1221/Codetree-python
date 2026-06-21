import sys
input = sys.stdin.readline
n, m = map(int, input().split())
seg = [tuple(map(int, input().split())) for _ in range(m)]
seg.sort()

def calc(seg, n, d):
    count = 0
    last = None
    for s, e in seg:
        pos = s if count == 0 else max(s, last + d)
        if pos > e:
            continue
        k = (e - pos) // d + 1     
        count += k
        last = pos + (k - 1) * d   
        if count >= n:
            return True
    return count >= n

low, high = 1, seg[-1][1] - seg[0][0]
ans = 0
while low <= high:
    mid = (low + high) // 2
    if calc(seg, n, mid):
        ans = mid
        low = mid + 1
    else:
        high = mid - 1
print(ans)