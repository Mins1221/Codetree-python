n,k = map(int,input().split())
result = 0
x = 0
points = []
for _ in range(n):
    m,d = tuple(input().split())
    m = int(m)
    if d == 'R':
        points.append((x,x+m))
        x +=m
    else:
        points.append((x-m,x))
        x -=m

positions = []
for x1,x2 in points:
    positions.append((x1,+1))
    positions.append((x2,-1))

positions.sort()

sum_val = 0
for i, (x,v) in enumerate(positions):
    if sum_val >= k :
        pre_v, _ = positions[i-1]
        result += x - pre_v
    sum_val +=v

print(result)
