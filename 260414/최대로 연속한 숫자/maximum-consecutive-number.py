from sortedcontainers import SortedSet

n, m = map(int, input().split())
arr = list(map(int, input().split()))
s_num = SortedSet()
s_len = SortedSet()

s_num.add(-1)
s_num.add(n + 1)
s_len.add((-(n + 1), -1, n + 1))

for y in arr:
    s_num.add(y)
    
    idx = s_num.index(y)   # y의 위치
    x = s_num[idx - 1]     # 왼쪽 이웃
    z = s_num[idx + 1]     # 오른쪽 이웃

    s_len.remove((-(z - x - 1), x, z))
    s_len.add((-(y - x - 1), x, y))
    s_len.add((-(z - y - 1), y, z))

    print(-s_len[0][0])