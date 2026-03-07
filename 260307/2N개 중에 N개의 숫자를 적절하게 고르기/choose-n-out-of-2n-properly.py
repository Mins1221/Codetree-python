n = int(input())
num = list(map(int, input().split()))

# Please write your codet
total = sum(num)
result = float('inf')
def choose(idx,cnt,curr_sum):
    global result
    if cnt == n:
        diff = abs(2*curr_sum - total)
        result = min(result,diff)
        return
    if idx >= 2*n : 
        return
    choose(idx + 1, cnt + 1, curr_sum + num[idx])
    choose(idx + 1, cnt, curr_sum)
choose(0,0,0)
print(result)

