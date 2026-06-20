n = int(input())
intervals = [map(int,input().split()) for _ in range(n)]
N = 1100000
point= [0] * N
for x1,x2 in intervals:
    point[x1] +=1
    point[x2] -=1

sum_val = 0
count = 0
for x in range(1,N):
    sum_val += point[x]
    count = max(count,sum_val)
print(count)