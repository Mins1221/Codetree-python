import heapq

n = int(input())
arr = list(map(int, input().split()))

pq = arr[1:][:] 
heapq.heapify(pq)
total = sum(arr[1:])
to_remove = {}
max_avg = float('-inf')

for k in range(1, n-1):
    # 삭제 예약된 원소가 top에 있으면 제거
    while to_remove.get(pq[0], 0) > 0:
        val = heapq.heappop(pq)
        to_remove[val] -= 1

    avg = (total - pq[0]) / (n - k - 1)
    max_avg = max(max_avg, avg)

    # 다음 k로 이동: arr[k]를 삭제 예약
    total -= arr[k]
    to_remove[arr[k]] = to_remove.get(arr[k], 0) + 1

print(f"{max_avg:.2f}")