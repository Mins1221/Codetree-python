def solve():
    N, K, B = map(int, input().split())
    missing_nums = set()
    for _ in range(B):
        missing_nums.add(int(input()))  # 한 줄에 하나씩 입력

    exist = [0] * (N + 1)
    for i in range(1, N + 1):
        if i not in missing_nums:
            exist[i] = 1

    prefix = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix[i] = prefix[i - 1] + exist[i]

    min_add = K
    for l in range(1, N - K + 2):
        r = l + K - 1
        present_count = prefix[r] - prefix[l - 1]
        min_add = min(min_add, K - present_count)

    print(min(min_add, B))

solve()