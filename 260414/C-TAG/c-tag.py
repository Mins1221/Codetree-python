from itertools import combinations
n, m = map(int, input().split())

A = [input() for _ in range(n)]
B = [input() for _ in range(n)]
count = 0
for (i,j,k) in combinations(range(1, m+1), 3):
    set_a = set()
    set_b = set()
    for paper in A:
        set_a.add((paper[i-1], paper[j-1], paper[k-1]))
    for paper in B:
        set_b.add((paper[i-1], paper[j-1], paper[k-1]))
    if set_a & set_b == set():
        count += 1

print(count)
