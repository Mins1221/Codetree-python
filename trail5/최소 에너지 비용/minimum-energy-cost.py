n = int(input())
dist = list(map(int,input().split()))
cost = list(map(int,input().split()))
R= [0] * (n+1)

R[0] = cost[0]
for i in range(1,n):
    R[i] = min(R[i-1],cost[i])
ans=0
for i in range(n-1):
    ans += dist[i] * R[i]

print(ans)