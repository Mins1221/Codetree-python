from sortedcontainers import SortedDict
n = int(input())
sd = SortedDict()

for _ in range(n):
    line = input().split()
    cmd = line[0]
    if cmd =="add":
        k = int(line[1])
        v = int(line[2])
        sd[k] = v
    if cmd =="remove":
        k = int(line[1])
        sd.pop(k)
    if cmd =="find":
        k = int(line[1])
        if k in sd:
            print(sd[k])
        else:
            print("None")
    if cmd =="print_list":
        if sd:
            print(*sd.values())
        else:
            print("None")


