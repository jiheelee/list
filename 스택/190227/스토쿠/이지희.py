import sys
sys.stdin = open('input.txt','r')

def check(stoku):
    for l in stoku:
        line = [0]*10
        for num in l:
            line[num] += 1
        for idx in line:
            if idx == 2:
                return 0
    return 1

def check2(result):
    for i in result:
        if i == 0:
            return 0
    return 1


T = int(input())
for tc in range(1,T+1):
    stoku = [list(map(int,input().split())) for i in range(9)]
    column_list = []
    for i in range(9):
        a = []
        for j in range(9):
            a.append(stoku[j][i])
        column_list.append(a)
    square_list = []
    for k in range(0,9,3):
        for p in range(0,9,3):
            s = []
            for i in range(3):
                for j in range(3):
                    s.append(stoku[k+i][p+j])
            square_list.append(s)
    print(f'#{tc}',end=" ")
    print(check2([check(stoku),check(column_list),check(square_list)]))
