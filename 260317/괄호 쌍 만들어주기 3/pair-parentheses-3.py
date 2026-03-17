A = input()
b = [c for c in A if c == '(' or c == ')']
sum_diff = 0
cnt = 0
for i in range(len(b)):
    for j in range(i+1,len(b)):    
        if b[i] == '(' and b[j] == ')':
            cnt +=1

print(cnt)
            