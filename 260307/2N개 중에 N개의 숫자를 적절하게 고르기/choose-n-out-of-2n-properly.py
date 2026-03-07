from itertools import combinations
n = int(input())
num = list(map(int, input().split()))

# Please write your code here.
total = sum(num)
result = float('inf')
diff =0
for combo in combinations(num,n):
    diff = abs(2*sum(combo)-total)
    result = min(diff,result)

print(result)
