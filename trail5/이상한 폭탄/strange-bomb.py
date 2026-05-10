n, k = map(int,input().split())

booms = [
    int(input()) for _ in range(n)
]

ans = -1

booms_dict = {}

for i in range(n):
    cnt_n = booms[i]
    booms_dict[cnt_n] = booms_dict.get(cnt_n, 0) + 1

    if i > k:
        out_n = booms[i-k-1]
        booms_dict[out_n] -= 1
    
    if booms_dict[cnt_n] > 1:
        ans = max(ans, cnt_n)


print(ans)
