import sys
sys.stdin = open('input.txt','r')

for t in range(1,11):
    tc = int(input())
    s_list = []
    for i in range(100):
        s_list.append(input())

    c_list = []

    for i in range(100):
        r = ""
        for j in range(100):
            r += s_list[j][i]
        c_list.append(r)

    result = ""

    for length in range(100, 0, -1):
        for s in s_list:
            for i in range(100-length+1):
                if s[i:i + length] == s[i:i + length][::-1]:
                    result = s[i:i + length]
        if result != "":
            break
        for c in c_list:
            for i in range(100-length+1):
                if c[i:i + length] == c[i:i + length][::-1]:
                    result = c[i:i + length]
        if result != "":
            break

    print("#",end="")
    print(tc,end=" ")
    print(len(result))



