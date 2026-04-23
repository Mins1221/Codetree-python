import heapq
n = int(input())
x = [int(input()) for _ in range(n)]

pq = []

for i in x:
    if i == 0:
        if pq:
            val = heapq.heappop(pq)
            print(val)
            pass
        else:
            print(0)
    else:
        heapq.heappush(pq,i)
        
