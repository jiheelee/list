import sys
sys.stdin = open('input.txt','r')

def rotation(num_list,N):
    result = [[0]*N for i in range(N)]
    for i in range(N):
        for j in range(N):
            result[j][abs(i-(N-1))] = num_list[i][j]
            
    return result
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    base = []
    for i in range(N):
        base.append(list(map(int, input().split())))
    rotation_1 = rotation(base,N)
    rotation_2 = rotation(rotation_1,N)
    rotation_3 = rotation(rotation_2,N)
    print("#",end="")
    print(tc)
    for i in range(N):
        r1 = "".join(list(map(str,rotation_1[i])))
        r2 = "".join(list(map(str, rotation_2[i])))
        r3 = "".join(list(map(str, rotation_3[i])))
        print(f'{r1} {r2} {r3}')
