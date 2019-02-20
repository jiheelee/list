import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split())
    complete = list(map(int,input().split()))
    not_complete = []

    for i in range(1,N+1):
        if i not in complete:
            not_complete.append(str(i))

    print("#",end="")
    print(tc,end=" ")
    print(" ".join(not_complete))