from itertools import permutations
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    num_list = [list(map(int,input().split())) for i in range(N)]
    column_list = []
    for p in permutations(range(N)):
        column_list.append(p)
    sum_list = []
    for c in range(len(column_list)):
        sum_num = 0
        for n in range(N):
            sum_num += num_list[n][column_list[c][n]]
        sum_list.append(sum_num)

    print(f'#{tc} {min(sum_list)}')
