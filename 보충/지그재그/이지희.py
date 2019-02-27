import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    num_list = list(map(int, input().split()))
    for i in range(9, 0, -1):
        for j in range(i):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
    result = sum(num_list[1:9])/8
    print(f"#{tc} %.0f"% result)

