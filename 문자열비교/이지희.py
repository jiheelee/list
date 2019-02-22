T = int(input())
for tc in range(1,T+1):
    inside = str(input())
    outside = str(input())
    inside_len = len(inside)
    outside_len = len(outside)
    i = 0
    j = 0
    while j < inside_len and i < outside_len:
        if inside[j] != outside[i]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1
    print("#",end="")
    print(tc,end=" ")
    if j == inside_len:
        print(1)
    else:
        print(0)