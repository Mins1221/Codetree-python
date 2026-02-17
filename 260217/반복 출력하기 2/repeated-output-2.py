n = int(input())

def print_HW(n):
    if n ==0:
        return

    print_HW(n-1)    
    print("HelloWorld")
# Please write your code here.

print_HW(n)