n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

# Please write your code here.
def choose(curr_turn,horses,score):
    if curr_turn == n:   
        return score


    max_score = 0

    for i in range(k):
        new_horses = horses[:]
        new_horses[i] += nums[curr_turn]
        # M까지 도달했는지 확인
        new_score = score
        if new_horses[i] >= m and horses[i] <m:
            new_score += 1
        max_score = max(max_score,choose(curr_turn+1,new_horses,new_score))      

    return max_score 

   
horses = [1] * k  # 전역에서 초기화 후 호출
choose(0, horses, 0)

print(choose(0, horses, 0))
        
