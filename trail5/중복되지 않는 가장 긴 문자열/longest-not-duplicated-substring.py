word = input()
n = len(word)
j = -1
ans =0
count = {}
for i in range(n):
    while j+1 < n and count.get(word[j+1],0) != 1:
        count[word[j+1]] = count.get(word[j+1],0) + 1
        j +=1
    ans = max(ans,j-i+1)
    count[word[i]] -= 1
print(ans)