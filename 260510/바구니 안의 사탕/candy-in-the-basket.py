
n, k = tuple(map(int, input().split()))
candies = [(-1, -1)]
for _ in range(n):
    cnt, x = tuple(map(int, input().split()))
    candies.append((x, cnt))

def get_pos_of_candy(candy_idx):
    x, _ = candies[candy_idx]
    return x

def get_num_of_candy(candy_idx):
    _, cnt = candies[candy_idx]
    return cnt


candies.sort()
ans = 0
total_nums = 0
j = 0
for i in range(1, n + 1):
    # 구간의 크기가 2K보다 같거나 작은 경우에 한하여 최대로 진행합니다.
    while j + 1 <= n and get_pos_of_candy(j + 1) - get_pos_of_candy(i) <= 2 * k:
        total_nums += get_num_of_candy(j + 1)
        j += 1
    
    # 현재 구간 [i, j]는 
    # i를 시작점으로 하는
    # 가장 긴 구간이므로
    # 구간 내 최대 사탕의 수를 갱신해줍니다.
    ans = max(ans, total_nums)

    # 다음 구간으로 넘어가기 전에
    # i번째에 해당하는 사탕을 구간에서 제외시킵니다.
    total_nums -= get_num_of_candy(i)

print(ans)
