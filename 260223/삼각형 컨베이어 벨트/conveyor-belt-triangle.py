n, t = map(int, input().split())

l = list(map(int, input().split()))
r = list(map(int, input().split()))
d = list(map(int, input().split()))

# Please write your code here.

# Please write your code here.
for _ in range(t):
    temp1 = l[n-1]
    temp2 = r[n-1] 
    temp3 = d[n-1]


    for i in range(n-1,0,-1):
        l[i] = l[i-1]
    l[0] = temp3

    for i in range(n-1,0,-1):
        r[i] = r[i-1]
    r[0] = temp1

    for i in range(n-1,0,-1):
        d[i] =d[i-1]
    d[0] = temp2



print(*l)
print(*r)
print(*d)