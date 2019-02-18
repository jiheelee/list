def subset(binary):
    for i in range(len(binary)):
        if binary[i] == 1:
            print(A[i],end=" ")
        print()

A = [1,2,3,4]

for i in range(16):
    binary = bin(i).split()
    print(binary)
    subset(binary)