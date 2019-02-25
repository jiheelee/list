T = int(input())
for i in range(T):
    D, A, B, F = map(int,input().split())
    speed = A + B
    result = (D / speed) * F
    print(f'#{i+1} {result}')