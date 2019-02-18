N = int(input())
arr = [list(map(int,input().split())) for i in range(N)]

# 배열 요소  0<ai<100인 조건
maxV = 0
maxI = 0
maxJ = 0
minI = 0
minJ = 0
minV = 100
# 최대값의 인덱스와 최대값
#최소값의 인덱스와 최소값


for i in range(N):
    for j in range(N):
        if(arr[maxI][maxJ]<arr[i][j]):
            maxI = i
            maxJ = j
        if(arr[minI][minJ]>arr[i][j]):
            minI = i
            minJ = j
print(maxI, maxJ, arr[maxI][maxJ])
print(minI, minJ, arr[minI][minJ])

