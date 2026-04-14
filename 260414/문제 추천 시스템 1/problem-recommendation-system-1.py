from sortedcontainers import SortedSet
n = int(input())
P, L = [], []
s = SortedSet()
for _ in range(n):
    p, l = map(int, input().split())
    P.append(p)
    L.append(l)
for i in range(n):
    s.add((L[i],P[i]))
m = int(input())
commands = []
for _ in range(m):
    cmd = input().split()
    if cmd[0] == "rc":
        commands.append((cmd[0], int(cmd[1])))
        if cmd[1] == "1":
            print(s[-1][1])
        if cmd[1] =="-1":
            print(s[0][1])
    else:
        commands.append((cmd[0], int(cmd[1]), int(cmd[2])))
        if cmd[0] =="ad":
            s.add((int(cmd[2]), int(cmd[1])))
        if cmd[0] =="sv":
            s.remove((int(cmd[2]), int(cmd[1])))


