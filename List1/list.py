T = int(input())
for tc in range(1,T+1)
    N = int(input())
    num_list = list(map(int,input().split()))

    result = max(num_list) - min(num_list)

    print("#",end="")
