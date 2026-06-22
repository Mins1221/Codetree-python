import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1

    events = []
    for _ in range(n):
        s = int(data[idx]); e = int(data[idx + 1]); idx += 2
        events.append((s, 0))   # 0 = 체크인
        events.append((e, 1))   # 1 = 체크아웃

    # (날짜, 타입) 정렬 → 같은 날이면 체크인(0)이 체크아웃(1)보다 앞
    # 즉, 같은 날 나가고 들어오는 두 사람을 동시에 카운트하게 됨
    events.sort()

    cur = 0   # 현재 사용 중인 방 수
    ans = 0   # 최대 동시 사용량
    for day, typ in events:
        if typ == 0:
            cur += 1
            ans = max(ans, cur)
        else:
            cur -= 1

    print(ans)

main()
