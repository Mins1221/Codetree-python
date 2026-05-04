N, K = map(int, input().split())
M = []
dir = []
positions = [0]
cur = 0 
for _ in range(N):
    m, d = input().split()
    m = int(m)
    M.append(int(m))
    dir.append(d)
for i in range(N): 
    if dir[i] == 'R':
        cur += M[i]
    else:
        cur -= M[i]
    positions.append(cur)
event = {}
for i in range(N):
    l  =min(positions[i],positions[i+1])
    r = max(positions[i],positions[i+1])
    event[l] = event.get(l,0) + 1
    event[r] = event.get(r,0) - 1

coords = sorted(event.keys())
result  = 0
cumsum = 0
for i in range(len(coords)-1):
    cumsum += event[coords[i]]
    length = coords[i+1] - coords[i]
    if cumsum >= K :
        result += length

print(result)