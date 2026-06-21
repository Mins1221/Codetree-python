import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# 1~n번 정점의 종류. 실제 입력 형식에 맞춰 이 한 줄만 조정하세요.
# 예: "0 1 1 0 ..." 형태로 종류가 한 줄에 주어진다고 가정
color = [None] + input().split()

edges = [tuple(map(int, input().split())) for _ in range(m)]

uf = list(range(n + 1))
def find(x):
    while uf[x] != x:
        uf[x] = uf[uf[x]]      # 경로 압축 (반복문 → 재귀 깊이 걱정 X)
        x = uf[x]
    return x
def union(x, y):
    X, Y = find(x), find(y)
    if X == Y:
        return False
    uf[X] = Y
    return True

ans = 0
cnt = 0                         # 실제로 사용한 간선 수
edges.sort(key=lambda e: e[2])
for a, b, cost in edges:
    if color[a] == color[b]:    # 같은 종류를 잇는 간선은 사용 불가
        continue
    if union(a, b):
        ans += cost
        cnt += 1

print(ans if cnt == n - 1 else -1)   # n-1개 못 채우면 트리 불가능