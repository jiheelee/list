import sys
sys.stdin = open('input.txt','r')

T = int(input())

for tc in range(1,T+1):
    case = str(input())
    num_list = list(input().split())
    language = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in range(len(num_list)):
        for j in range(len(language)):
            if num_list[i] == language[j]:
                num_list[i] = number[j]

    num_list.sort()

    for i in range(len(num_list)):
        for j in range(len(number)):
            if num_list[i] == number[j]:
                num_list[i] = language[j]

    print(f"#{tc}")
    print(" ".join(num_list))




