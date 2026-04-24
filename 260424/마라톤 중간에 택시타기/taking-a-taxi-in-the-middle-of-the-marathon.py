n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

def dist(i, j):
    return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
L = [0] * n
R = [0] * n
for i in range(1, n):
    L[i] = L[i-1] + dist(i-1, i)

for i in range(n-2, -1, -1):
    R[i] = R[i+1] + dist(i, i+1)

ans = float('inf')
for i in range(1, n-1):
    ans = min(ans, L[i-1] + R[i+1] + dist(i-1, i+1))

print(ans)

