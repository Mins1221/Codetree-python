import heapq
N = int(input())
commands = []
class PriorityQueue:
    def __init__(self):          # 빈 Priority Queue 하나를 생성합니다.
        self.items = []
                
    def push(self, item):        # 우선순위 큐에 데이터를 추가합니다.
        heapq.heappush(self.items, -item)
                
    def empty(self):             # 우선순위 큐가 비어있으면 True를 반환합니다.
        return not self.items
                
    def size(self):              # 우선순위 큐에 있는 데이터 수를 반환합니다.
        return len(self.items)
        
    def pop(self):               # 우선순위 큐에 있는 데이터 중 최댓값에 해당하는 데이터를 반환하고 제거합니다.
        if self.empty():
            raise Exception("PriorityQueue is empty")
            
        return -heapq.heappop(self.items)
                
    def top(self):               # 우선순위 큐에 있는 데이터 중 최댓값에 해당하는 데이터를 제거하지 않고 반환합니다.
        if self.empty():
            raise Exception("PriorityQueue is empty")
                        
        return -self.items[0]


pq = PriorityQueue()          # 우선순위 큐를 선언합니다. => 빈 우선순위 큐
for _ in range(N):
    line = input().split()
    cmd = line[0]
    
    if cmd == "push":
        pq.push(int(line[1]))
        pass
    elif cmd == "pop":
        print(pq.pop())
        pass
    elif cmd == "size":
        print(pq.size())
        pass
    elif cmd =="empty":
        print(1 if pq.empty() else 0)
    elif cmd =="top":
        print(pq.top()) 


