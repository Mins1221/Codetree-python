n = int(input())
commands = []
x = []
s = set()
for _ in range(n):
    cmd, val = input().split()
    commands.append(cmd)
    x.append(int(val))
    if cmd == "add":
       s.add(val)
    if cmd =="remove":
        s.remove(val)
    if cmd=="find":
        if val in s:
            print("true")
        else:
            print("false")


