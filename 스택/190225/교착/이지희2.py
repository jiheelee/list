import sys
sys.stdin = open('input.txt','r')

for tc in range(1, 11):
    l = int(input())
    t = [list(map(int, input().split())) for i in range(100)]

    cnt = 0
    a = [0] * 100
    for i in range(100):
        for j in range(100):
            if (a[j] == 0 and t[i][j] == 1):
                a[j] = 1
            elif (a[j] == 1 and t[i][j] == 2):  # 교착
                cnt += 1
                a[j] = 2
            elif (a[j] == 2 and t[i][j] == 1):
                a[j] = 1
    print('#{} {}'.format(tc, cnt))

# for tc in range(1,11):
#     N = int(input())
#     num_list = [list(map(int,input().split())) for i in range(N)]
#     result = [0]*N
#     count = 0
#     for r in range(N):
#         for c in range(N):
#             if (num_list[c][r] == 1 and result[c] == 0):
#                 result[c] = 1
#             elif (num_list[c][r] == 2 and result[c] == 1):
#                 count += 1
#                 result[c] = 0
#
#     print(count)







