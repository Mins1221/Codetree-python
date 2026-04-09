n, m = map(int, input().split())
words= [input() for _ in range(n)]
d = {}
cnt=1
for i in words:
    d[i] = cnt
    cnt+=1

for _ in range(m):
    inp = input()
    if inp not in d:
        inp = int(inp)
        print(words[inp-1])
    else:
        print(d[inp])
