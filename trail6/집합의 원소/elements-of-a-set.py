n,m = map(int,input().split())
uf = [0] * (n+1)
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
for _ in range(m):
    type,a,b, = map(int,input().split())
    if type == 0 :
        union(a,b)
    else:
        if find(a) == find(b):
            print(1)
        else:
            print(0)

