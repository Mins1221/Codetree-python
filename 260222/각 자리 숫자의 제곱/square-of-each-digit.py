n = int(input())

# Please write your code here.

def fact(n):
    if n <10:
        return n **2

    return fact(n//10) + (n%10) **2

print(fact(n))

  


