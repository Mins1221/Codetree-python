import heapq

n = int(input())
arr = list(map(int, input().split()))

max_avg = float('-inf')

for k in range(1, n-1):  # k: 1 이상 N-2 이하
    pq = arr[k:][:]       # arr[k:]를 매번 새로 힙으로
    heapq.heapify(pq)
    
    min_val = heapq.heappop(pq)  # 최솟값 제거
    total = sum(pq)               # 남은 합
    avg = total / len(pq)
    
    max_avg = max(max_avg, avg)

print(f"{max_avg:.2f}")