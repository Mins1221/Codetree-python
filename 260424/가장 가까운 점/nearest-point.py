import heapq
n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]
pq = []
# Please write your code here.
for x,y in points:
    heapq.heappush(pq,(x+y,x,y))

for i in range(m):
    i,x,y = heapq.heappop(pq)

    x,y = x+2,y+2
    heapq.heappush(pq,(x+y,x,y))

_, x,y = pq[0]
print(x,y)