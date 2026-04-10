from sortedcontainers import SortedDict
n = int(input())
words = [input() for _ in range(n)]
sd = SortedDict()
cnt = 1

for elem in words:
    if elem not in sd:
        sd[elem] = 1
    else:
        sd[elem] += 1

for key, value in sd.items():
    ratio = value / n  *100    # 비율 계산
    print(f"{key} {ratio:.4f}") 