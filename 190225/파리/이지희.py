import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    area = [list(map(int,input().split())) for i in range(N)]
    # sum_list = []
    max_num = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum_square = 0
            for k in range(M):
                sum_square += sum(area[i+k][j:j+M])
            # sum_list.append(sum_square)
            if sum_square > max_num:
                max_num = sum_square
    result = max_num
    # result = max(sum_list)
    print(f'#{tc} {result}')