n = int(input())
intervals = [tuple(map(int,input().split())) for _ in range(n)]
N = 1000000
points= [0] * N
for x1,x2 in intervals:
    points[x1] +=1
    points[x2] -=1


count = 0
max_val = 0

for x in range(1,N):
    max_val += points[x]
    count = max(count,max_val)

print(count)
