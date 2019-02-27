import sys
sys.stdin = open('input.txt','r')


T = int(input())
for tc in range(1,T+1):
    t = int(input())
    score_count = [0] * 101
    num_list = list(map(int, input().split()))
    for i in num_list:
        score_count[i] += 1
    max_count = 0
    max_idx = 1
    for i in range(len(score_count)):
        if score_count[i] >= max_count:
            max_count = score_count[i]
            max_idx = i

    print(f'#{tc} {max_idx}')