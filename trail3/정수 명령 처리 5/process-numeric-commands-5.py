N = int(input())


num =   []

for _ in range(N):
    line = input().split()
    cmd = line[0]

    if cmd == "push_back":
        num.append(int(line[1]))
    elif cmd == "pop_back":
        num.pop()
    elif cmd == "size":
        print(len(num))
    elif cmd == "get":
        print(num[int(line[1])-1])


