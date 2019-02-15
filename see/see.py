import sys
sys.stdin = open("input.txt",'r')
tc = 0
for i in range(10):
    tc += 1
    N = int(input())
    b = list(map(int,input().split()))
    result = 0
    for i in range(2,N-2):
        a = min(b[i]-b[i-2],b[i]-b[i-1],b[i]-b[i+1],b[i]-b[i+2])
        if a > 0:
            result += a
    print('#', end="")
    print(tc,end=" ")
    print(result)