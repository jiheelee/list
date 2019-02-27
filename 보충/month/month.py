import sys
sys.stdin = open('input.txt','r')

T = int(input())
d = [0,31,28,31,30,31,30,31,31,30,31,30,31]
for tc in range(1,T+1):
    m1, d1, m2, d2 = map(int,input().split())
    day2=0
    day1=0
    for i in range(m2):
        day2 += d[i]
    for j in range(m1):
        day1 += d[j]
    print(f'#{tc} {(day2+d2)-(day1+d1) + 1}')
