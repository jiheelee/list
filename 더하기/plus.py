T = int(input())
for tc in range(1,T+1):
    N = int(input())
    num_list = list(map(int,input().split()))
    sum_list=[]
    for length in range(1,N+1):
        for i in range(N-length,-1,-1):
            part = 0
            for j in range(length):
                part += num_list[j]
            sum_list.append(part)


    result = max(sum_list)
    print(result)



