for tc in range(10):
    N = int(input())

    my_list = []
    for i in range(100):
        my_list.append(list(map(int, input().split())))
    sum_row = 0
    for j in range(100):
        row = sum(my_list[j])
        if row > sum_row:
            sum_row = row
    sum_column = 0
    for k in range(100):
        s = 0
        for m in range(100):
            s += my_list[m][k]
        if s > sum_column:
            sum_column = s

    sum_cross = 0
    for t in range(100):
        sum_cross += my_list[t][t]

    result = max(sum_row, sum_column, sum_cross)

    print("#", end="")
    print(N, end=" ")
    print(result)