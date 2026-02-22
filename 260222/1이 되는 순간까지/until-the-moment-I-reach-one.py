n = int(input())

# Please write your code here.
def count(n):
    if  n ==1 :
        return 0
    if n % 2 ==0:

        return 1 +count(n //2)
    else :
  
        return 1+ count(n// 3)


print(count(n))
    




