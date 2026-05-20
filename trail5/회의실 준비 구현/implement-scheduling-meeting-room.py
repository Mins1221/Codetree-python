n = int(input())
arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]
arr.sort(key=lambda x: x[1])
last_e, ans = -1, 0
for s, e in arr:
    if last_e <= s:
        last_e = e
        ans += 1

print(ans)

