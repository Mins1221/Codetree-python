n = int(input())
# 이렇게 하면 시작점과 끝점이 항상 함께 다녀요
segments = []
for _ in range(n):
    a, b = map(int, input().split())
    segments.append((a, b))  # (시작, 끝) 쌍으로 저장

# Please write your code here.

segments.sort(key=lambda i: i[1]) # 오름차순 정렬 완료

count = 0
last_end = -1

for i in segments :
    if i[0] > last_end :
        count +=1
        last_end = i[1]

print(count)