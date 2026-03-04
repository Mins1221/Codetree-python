n, m = map(int, input().split())
answer = []
# Please write your code here.

def choose(curr_num, cnt):
    if cnt == m:
        print(*answer)
        return

    for i in range (curr_num, n+1):
        answer.append(i)
        choose(i + 1, cnt+1)
        answer.pop()

    return 

choose(1,0)


