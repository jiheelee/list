import sys
sys.stdin = open('input.txt','r')

for tc in range(1,11):
    N = int(input())
    num_list = [input().split() for i in range(N)]
    c_list = []
    for i in range(N):
        s =""
        for j in range(N):
            s += num_list[j][i]
        c_list.append(s)

    re_list = []
    for i in c_list:
         re_list.append(i.replace("0",""))
    count = 0
    for i in re_list:
        count_1 = i.count("12")
        count += count_1
    print(f'#{tc} {count}')