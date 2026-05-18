import sys

n, m = map(int, sys.stdin.readline().split())
jewels = []

for _ in range(n):
    w, v = map(int, sys.stdin.readline().split())
    ratio = v / w 
    jewels.append([w, v, ratio]) 

jewels.sort(key=lambda x: x[2], reverse=True) 

total = 0 
for jewel in jewels:
    w, v = jewel[0], jewel[1]
    
    if m == 0:
        break

    else:
        if m >= w:
            m -= w
            total += v
        
        else:
            total += v * (m / w)
            m = 0 

print(f'{total:.3f}')
