n, m, k = map(int, input().split())
uf = [0] *(n+1)
for i in range(1,n+1):
    uf[i] = i
def find(x):
    if uf[x] == x:
        return x
    uf[x] = find(uf[x])
    return uf[x]
def union(x,y):
    X,Y = find(x), find(y)
    uf[X] = Y
for _ in range(m):
    a,b = tuple(map(int,input().split()))
    union(a,b)
is_pos =True
path = [0] + list(map(int,input().split()))
for i in range(1,k):
    if find(path[i]) != find(path[i+1]):
        is_pos = False
if is_pos:
    print(1)
else:
    print(0)