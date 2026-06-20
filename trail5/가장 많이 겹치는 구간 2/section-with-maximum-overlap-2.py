n = int(input())
intervals = [tuple(map(int,input().split())) for _ in range(n)]

points= []
for x1,x2 in intervals:
    points.append((x1,+1))
    points.append((x2,-1))

points.sort()
count = 0
max_val = 0

for x,v in points:
    max_val += v
    count = max(count,max_val)

print(count)
