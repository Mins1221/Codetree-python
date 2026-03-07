n = int(input())
num = list(map(int, input().split()))
  
def choose(curr_num,cnt):
    global result
    if curr_num >= (n-1):
        result = min(result, cnt)
        return 
    if num[curr_num] == 0:
        return
    for i in range(1,num[curr_num]+1):
        next = curr_num + i
        if next <= (n-1):
            choose(next,cnt+1)

result = float('inf')
choose(0,0)
if result == float('inf'):
    result = -1
print(result)