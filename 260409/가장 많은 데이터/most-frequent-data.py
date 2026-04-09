n = int(input())
words = [input() for _ in range(n)]

# Please write your code here.
cnt = {}
for elem in words:
    if elem not in cnt:
        cnt[elem] = 1
    else:
        cnt[elem]+=1
    
print(max(cnt.values()))
