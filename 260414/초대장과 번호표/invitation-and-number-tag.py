from collections import deque

N, G = map(int, input().split())

groups = []
person_to_groups = [[] for _ in range(N + 1)]  

for i in range(G):
    nums = list(map(int, input().split()))
    members = set(nums[1:])
    groups.append(members)
    for p in members:
        person_to_groups[p].append(i)  

invited = set()
invited_count = [0] * G 
queue = deque([1])
invited.add(1)

while queue:
    person = queue.popleft()
    for gi in person_to_groups[person]:       
        invited_count[gi] += 1
        if invited_count[gi] == len(groups[gi]) -1:  
            for p in groups[gi]:
                if p not in invited:
                    invited.add(p)
                    queue.append(p)            

print(len(invited))
