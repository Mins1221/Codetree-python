N, G = map(int, input().split())

group = []
group_size = []
groups = set()
for _ in range(G):
    nums = list(map(int, input().split()))
    group_size.append(nums[0])
    group.append(nums[1:])

invited = set([1])

while True:
    changed = False
    for i in group:
        notInvited = set(i) - invited
        if len(notInvited) == 1:
            invited.add(next(iter(notInvited)))
            changed = True
        
    if not changed :
        break

    
print(len(invited))
