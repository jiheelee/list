import sys
sys.stdin = open('input.txt','r')

T = int(input())

for tc in range(1,T+1):
    P, A, B = map(int, input().split())
    def search(start,end,goal):
        count = 0
        middle = 0
        while middle != goal:
            middle = int((start + end) / 2)
            if goal < middle:
               end = middle
            else:
                start = middle
            count += 1
        return count

    count_A = search(1,P,A)
    count_B = search(1,P,B)
    if count_A < count_B:
        print("#",end="")
        print(tc,end=" ")
        print("A")
    elif count_B < count_A:
        print("#", end="")
        print(tc, end=" ")
        print("B")
    else:
        print("#", end="")
        print(tc, end=" ")
        print(0)