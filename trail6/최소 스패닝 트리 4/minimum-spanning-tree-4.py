n,m = map(int,input().split())
uf = [0] *(n+1)
type = [' '] + list(input().split())
edges = [tuple(map(int,input().split())) for  _ in range(m)]
for i in range(1,n+1):
    uf[i] = i
def find(x):
    if uf[x] == x:
        return x
    uf[x] = find(uf[x])
    return uf[x]
def union(x,y):
    X,Y = find(x),find(y)
    uf[X] = Y
ans =0
edges.sort(key = lambda x:x[2])
for x,y,cost in edges:
    if type[x] == type[y]:
        continue
    if find(x) != find(y):
        ans += cost
        union(x,y)
is_all_connected = True
for i in range(2,n+1):
    x = find(x)
    y = find(y)
    if x!=y:
        is_all_connected = False
if is_all_connected :
    print(ans)
else:
    print(-1)