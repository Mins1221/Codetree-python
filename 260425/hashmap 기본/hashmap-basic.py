n = int(input())
commands = []
d = dict()
for _ in range(n):
    line = input().split()
    cmd = line[0]
    k = int(line[1])
    if cmd == "add":
        v = int(line[2])
        commands.append((cmd, k, v))
        d[k] = v
    else:
        commands.append((cmd, k))
        if cmd =="remove":
            d.pop(k)
        if cmd =="find":
            if k in d:
                print(d[k])
            else:
                print("None")