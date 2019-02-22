import sys
sys.stdin = open("input.txt","r")

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    string = [input().split() for i in range(N)]
    result = ""
    while result == "":
        for i in range(N):
            for j in range(N-M+1):
                k = "".join(string[i])[j:j+M]
                if k == k[::-1]:
                    result = k
            for m in range(N-M+1):
                s = ""
                for j in range(M):
                       s += "".join(string[m+j])[i]
                if s == s[::-1]:
                    result = s
    print("#",end="")
    print(tc,end=" ")
    print(result)