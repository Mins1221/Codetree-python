# 입력 받기
n, k = map(int, input().split())

baskets = []
for _ in range(n):
    cnt, x = map(int, input().split())
    baskets.append((x, cnt))

baskets.sort()


sum_candy = 0
current_candy= 0
left = 0

for right in range(n):  # right (구간의 끝점)
    current_candy += baskets[right][1]
    while baskets[right][0] - baskets[left][0] > 2 * k: # 구간을 벗어나면
        current_candy -= baskets[left][1]
        left += 1
    sum_candy = max(sum_candy, current_candy)
print(sum_candy)
