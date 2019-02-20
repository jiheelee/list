T = int(input())

for tc in range(1,T+1):
    a, b, c, d = map(int,input().split())
    hour = a + c
    minute = b + d
    if b + d >= 60:
        hour += 1
        minute -= 60
    if hour > 12:
        hour -= 12
    print(f'#{tc} {hour} {minute}')


