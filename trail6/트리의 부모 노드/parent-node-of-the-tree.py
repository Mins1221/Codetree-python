import sys
# input = sys.stdin.readline

tree_parent = {}
n = int(input())

for i in range(n-1):
    a, b = map(int, input().split())
    tree_parent[b] = a
for i in range(2, n + 1):
    print(tree_parent[i])
