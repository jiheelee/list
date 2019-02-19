#import sys
#sys.stdin = open('sample_input (8).txt','r')

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
T = int(input())
n = len(A)
for tc in range(1, T+1):
    # print(tc)
    N, K = map(int, input().split())
    print(tc, N, K)
    total_list = []

    for i in range(1<<n):
        subset_list = []
        for j in range(n+1):
            if i & (1<<j):
                subset_list.append(A[j])
        total_list.append(subset_list)
    count = 0
    for i in total_list:
        if len(i)==N and sum(i)==K:
            count += 1


    print("#", end="")
    print(tc, end=" ")
    print(count)


