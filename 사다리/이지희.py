import sys
sys.stdin = open('input.txt','r')

for tc in range(1,11):
    tn = int(input())
    ladder = [list(map(int,input().split())) for i in range(100)]
    x = ladder[99].index(2)
    y = 98
    turn = "where"
    while y > 0:
        if x >= 1 and ladder[y][x-1] == 1 and turn != "right":
            x = x-1
            turn = "left"
        elif x <= 98 and ladder[y][x+1] == 1 and turn != "left":
            x = x + 1
            turn = "right"
        else:
            y = y - 1
            turn = "where"

    print("#",end="")
    print(tc,end=" ")
    print(x)