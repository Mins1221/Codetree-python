from sortedcontainers import SortedSet

T = int(input())

for _ in range(T):          # T번 반복
    s = SortedSet()         # 테스트케이스마다 초기화
    k = int(input())
    operations = [tuple(input().split()) for _ in range(k)]

    for op in operations:   # 각 명령어 바로 실행
        cmd = op[0]
        n = int(op[1])

        if cmd == "I":
            s.add(n)
        elif cmd == "D":
            if s:           # 비어있으면 무시
                if n == 1:
                    s.remove(s[-1])  # 최댓값 삭제
                else:
                    s.remove(s[0])   # 최솟값 삭제

    if s:
        print(s[-1], s[0])  # 최댓값 최솟값
    else:
        print("EMPTY")