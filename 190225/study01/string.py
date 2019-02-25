import sys
sys.stdin = open('input.txt','r', encoding='UTF8')

for tc in range(1,11):
    tn = int(input())
    s1 = input()
    s2 = input()
    num = s2.count(s1)
    print(f'#{tn} {num}')