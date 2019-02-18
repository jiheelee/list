import sys
sys.stdin = open('test.txt','r')

N = int(input())
arr = [list(map(int,input().split())) for i in range(N)]

result = 0

for i in range(N):
    for j in range(N):
        top = 0
        bottom = 0
        left = 0
        right = 0
        if i > 0:
            top = abs(arr[i][j] - arr[i-1][j])
        if i < N-1:
            bottom = abs(arr[i][j] - arr[i+1][j])
        if j > 0:
            left = abs(arr[i][j] - arr[i][j-1])
        if j < N-1:
            right = abs(arr[i][j] - arr[i][j+1])
        sum = top + bottom + left + right

        result = result + sum

print(result)