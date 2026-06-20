n= int(input())
intervals =[map(int,input().split()) for _ in range(n)]
point = [0] * (n+100)
count = 0
sum_val = 0
for x1,x2 in intervals:
    point[x1] +=1
    point[x2] -=1

for x in range(1,n+100):
    sum_val += point[x]
    count = max(count,sum_val)

print(count)