import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    box_area = [[0] * 10 for i in range(10)]
    def paint(r1, c1, r2, c2, color):
        c = 0
        for i in range(r1,r2+1):
            for j in range(c1,c2+1):
                box_area[i][j] += color

    N = int(input())
    for n in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        paint(r1, c1, r2, c2, color)
    count = 0
    for i in range(10):
        for j in range(10):
            if box_area[i][j] == 3:
                count += 1
    print("#",end="")
    print(tc,end=" ")
    print(count)