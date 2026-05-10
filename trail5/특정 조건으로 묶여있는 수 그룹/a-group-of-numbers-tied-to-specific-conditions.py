# 변수 선언 및 입력:
n, k = tuple(map(int, input().split()))
arr = [0] + [
    int(input())
    for _ in range(n)
]
L, R = [0] * (n + 1), [0] * (n + 1)

# 숫자들을 정렬해줍니다.
arr.sort()

# L 배열을 two pointer 방식을 통해 채워줍니다.
# L[i] = 1번부터 i번까지의 숫자들 중
#        정확히 조건을 만족하는 하나의 그룹을 만든다고 했을 때
#        포함할 수 있는 숫자의 개수 중 최댓값
max_num = 0
i = 1
for j in range(1, n + 1):
    # 구간 내 차이가 K를 넘는다면 계속 진행합니다.
    while i + 1 <= j and arr[j] - arr[i] > k:
        i += 1

    max_num = max(max_num, j - i + 1)


    L[j] = max_num

max_num = 0
j = n
for i in range(n, 0, -1):
    while j - 1 >= i and arr[j] - arr[i] > k:
        j -= 1
    
    max_num = max(max_num, j - i + 1)

    R[i] = max_num

ans = L[n]
for i in range(1, n):
    ans = max(ans, L[i] + R[i + 1])

print(ans)
