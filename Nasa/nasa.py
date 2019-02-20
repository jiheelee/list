import sys
sys.stdin = open('input.txt','r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    screw_list = list(map(int, input().split()))
    front = []
    back = []
    result = []

    for i in range(len(screw_list)):
        if i % 2:
            back.append(screw_list[i])
        else:
            front.append(screw_list[i])

    for i in range(len(front)):
        if front[i] not in back:
            start_index = i

    for i in range(len(front)):
        result.append(front[start_index])
        result.append(back[start_index])
        for j in range(len(back)):
            if back[start_index] == front[j]:
                start_index = j
    print("#",end='')
    print(tc,end=" ")
    print(result)
