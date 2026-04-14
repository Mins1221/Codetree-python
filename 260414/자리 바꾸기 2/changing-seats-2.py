n, k = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(k)]
seat = [0]
for i in range(1,n+1):
    seat.append(i)
visited = []
for i in range(n+1):
    visited.append({i}) 

for j in range(1,4):
    for l in edges:
        a,b = l[0], l[1]
        seat[a], seat[b] = seat[b], seat[a] 
        visited[seat[a]].add(a) 
        visited[seat[b]].add(b)

for s in range(1, n+1):
    print(len(visited[s]))