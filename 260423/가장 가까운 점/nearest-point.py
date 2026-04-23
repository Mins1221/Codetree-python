import heapq
n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
pq= []
for point in points:
    x,y = point
    heapq.heappush(pq,(x+y,x,y))

best_point = pq[0]
for _ in range(m):
    dist, x, y = heapq.heappop(pq)
    heapq.heappush(pq, (x+2+y+2, x+2, y+2))
_, x, y = pq[0]
print(x, y)