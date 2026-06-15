n = int(input())

parent = {}

for _ in range(n-1):
    a, b = map(int, input().split())
    parent[b] = a

for a in range(2, n+1):
    print (parent[a])
