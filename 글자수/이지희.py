import sys
sys.stdin = open('input.txt','r')

T = int(input())

for tc in range(1,T+1):
    str1 = str(input())
    str2 = str(input())
    word = ""
    for i in str1:
        if i not in word:
            word += i
    criteria = 0
    for i in str1:
        count = 0
        for j in range(len(str2)):
            if i == str2[j]:
                count += 1
        if count > criteria:
            criteria = count
    print("#",end="")
    print(tc,end=" ")
    print(criteria)