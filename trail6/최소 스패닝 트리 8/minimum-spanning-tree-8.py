n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
uf = list(range(n + 1))

def find(x):
    while uf[x] != x:
        uf[x] = uf[uf[x]]
        x = uf[x]

    return x

def union(x,y):
    X,Y = find(x), find(y)
    if X == Y:
        return False
    uf[Y] = X
    return True
edges.sort(key = lambda x: x[2])
answer = 0
cnt = 0
for u, v, w in edges:
    if union(u, v):
        answer += w
        cnt += 1
        if cnt == n - 1:
            break
print(answer)


