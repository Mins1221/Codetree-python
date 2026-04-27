k,n= map(int, input().split())
answer= []

def print_answer():
    for num in answer:
        print(num,end=" ")
    print()

def find(cnt):
    if cnt == n:
        print_answer()
        return

    for i in range(1,k+1):
        answer.append(i)
        find(cnt+1)
        answer.pop()

find(0)