from sortedcontainers import SortedSet
T = int(input())

for _ in range(T):
    s = SortedSet()
    k = int(input())
    operations = [tuple(input().split()) for _ in range(k)]
    for op in operations:
        cmd = op[0]
        n = int(op[1])
        if cmd =="I":
            s.add(n)
        if cmd =="D":
            if s:
                if n == 1:
                    s.remove(s[-1])
                else:
                    s.remove(s[0])
    if s:
        print(s[-1],s[0])
    else:
        print("EMPTY")
        
    # Please write your code here.
        
