from heapq import heappush, heappop
n, d = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]
points.sort()
max_heap = []
min_heap = []

now = dict()

i = 0
MAX = float('inf')
ans = MAX

for j in range(n):
    cur_y = points[j][1]
    heappush(max_heap, -cur_y)
    heappush(min_heap, cur_y)
    now[cur_y] = now.get(cur_y, 0) + 1

    while True:
        while max_heap and now.get(-max_heap[0], 0) == 0:
            heappop(max_heap)
        while min_heap and now.get(min_heap[0], 0) == 0:
            heappop(min_heap)

        if not max_heap or not min_heap:
            break

        if ( -max_heap[0] - min_heap[0] ) >= d: 
            ans = min(ans, points[j][0] - points[i][0]) 
            now[points[i][1]] -= 1
            i += 1
        else:
            break

if ans == MAX:
    ans = -1
print(ans)
    
    

