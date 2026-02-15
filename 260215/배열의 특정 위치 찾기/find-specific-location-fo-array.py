arr = list(map(int,input().split()))
n=len(arr)

sum_val = 0
three_val=[]
for i in range(1, n, 2):
    sum_val += arr[i]

for i in range(3,n,3):
    three_val.append(i)

avg_val = sum(three_val) / len(three_val)
print(sum_val, round(avg_val,1))
print(three_val)

