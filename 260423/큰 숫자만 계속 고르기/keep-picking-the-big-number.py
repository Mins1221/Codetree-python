import heapq
n, m = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
pq = []
for i in arr:
    heapq.heappush(pq,-i)

for j in range(m):
    val = heapq.heappop(pq)
    x = val +1
    heapq.heappush(pq,x)
    



print(-pq[0])