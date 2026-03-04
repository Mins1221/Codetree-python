n, m = map(int, input().split())
A = list(map(int, input().split()))
answer = []
# Please write your code here.
max_val =0
def choose(curr_num,cnt):
    global max_val
    if cnt == m:
        result = 0
        for num in answer:
            result = result ^ num
        max_val = max(max_val, result)
        return


    for i in range (curr_num, n):
        answer.append(A[i])
        choose(i + 1, cnt+1)
        answer.pop()


    return 

choose(0,0)
print(max_val)