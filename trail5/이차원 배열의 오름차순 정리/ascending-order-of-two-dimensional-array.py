# 변수 선언 및 입력:
n = int(input())
k = int(input())

low = 1                        
high = n * n                
ans = n * n                 

while low <= high:              
    mid = (low + high) // 2     
    val = 0
    for i in range(1, n + 1):
        val += min(n, mid // i)
    
    if val >= k:            
        high = mid - 1        
        ans = min(ans, mid)
    else:
        low = mid + 1      

print(ans)
