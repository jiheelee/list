N = 3
A = [1,2,3]
for i in range(2**N):
    for j in range(N-1, -1,-1):
        if(i&(1<<j) !=0):
            print(A[j], end='')
    print()