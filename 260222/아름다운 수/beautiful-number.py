n = int(input())

# Please write your code here.
count = 0

def find(cnt):
    global count
    if cnt == n:
        count +=1
        return 
    
    if cnt > n:
        return

    for i in range(1,5):
        find(cnt + i)

    

find(0)
print(count)