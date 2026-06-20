n,k = map(int,input().split())
x= 0
point=[]
for i in range(n):
    m,d = tuple(input().split())
    m = int(m)
    if d =='R':
        point.append((x,x+m))
        x +=m
    else:
        point.append((x-m,x))
        x-=m

positions=[]
for x1,x2 in point:
    positions.append((x1,+1))
    positions.append((x2,-1))
positions.sort()
sum_val = 0
result = 0
for i,(x,v) in enumerate(positions):
    if sum_val >= k:
        pre_x,_ = positions[i-1]
        result += x - pre_x
    sum_val +=v
print(result)