import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    word = str(input())
    result = 1
    N = len(word)
    for i in range(N//2):
        if word[i] != word[N-1-i]:
            result = 0

    print("#",end="")
    print(tc,end=" ")
    print(result)