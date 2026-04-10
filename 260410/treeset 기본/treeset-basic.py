from sortedcontainers import SortedSet
n = int(input())
s = SortedSet()

for _ in range(n):
    line = input().split()
    cmd = line[0]

    if cmd == "largest":
        print(s[-1] if s else "None")
    elif cmd == "smallest":
        print(s[0] if s else "None")
    else:
        k = int(line[1])
        if cmd == "add":
            s.add(k)
        elif cmd == "remove":
            s.remove(k)
        elif cmd == "find":
            print("true" if k in s else "false")
        elif cmd == "lower_bound":
            idx = s.bisect_left(k)
            print(s[idx] if idx < len(s) else "None")  # 첫 번째 k 이상인 값
        elif cmd == "upper_bound":
            idx = s.bisect_right(k)
            print(s[idx] if idx < len(s) else "None")