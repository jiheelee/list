def cal(num_list):
    a_list = []
    cal_list = []
    cnt1 = 0
    cnt2 = 0
    for n in num_list:
        if n == "*" or n== "+" or n=="-" or n=="/" or n==".":
            a_list.append(n)
            cnt1 += 1
        else:
            a_list.append(int(n))
            cnt2 += 1
    if cnt1 != cnt2:
        return "error"
    for a in a_list:
        if type(a) == type(1):
            cal_list.append(a)
        else:
            if a == "+":
                res = cal_list[-2] + cal_list[-1]
            elif a == "-":
                res = cal_list[-2] - cal_list[-1]
            elif a == "*":
                res = cal_list[-2] * cal_list[-1]
            elif a == "/":
                if cal_list[-1] == 0:
                    return "error"
                else:
                    res = cal_list[-2] // cal_list[-1]
            elif a == ".":
                return cal_list[0]
            cal_list.append(res)
            cal_list.pop(-2)
            cal_list.pop(-2)

T = int(input())
for tc in range(1,T+1):
    num_list = list(input().split())
    print(f'#{tc} {cal(num_list)}')