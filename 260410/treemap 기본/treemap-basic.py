from sortedcontainers import SortedDict
n = int(input())
sd = SortedDict()

for _ in range(n):
    line = input().split()
    cmd = line[0]

    if cmd == "print_list":
        if sd:
            print(*sd.values())  # 한 줄에 공백으로 출력
        else:
            print("None")        # 비어있으면 None
    else:
        k = int(line[1])
        if cmd == "add":
            v = int(line[2])
            sd[k] = v
        elif cmd == "remove":
            sd.pop(k)
        elif cmd == "find":
            print(sd[k] if k in sd else "None")