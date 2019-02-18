def search(arr, n, key):
    i = 0
    while (i<n and arr[i] !=key):
        i += 1
    if(i<n):
        return i
    else:
        return -1

def find(arr, n, key):
    for i in range(n):
        if(arr[i]==key):
            return i
    return -1

def bSearch(arr, n, key):
    start = 0
    end = n-1
    while(start<=end):
        middle =(start+end)//2
        if(arr[middle]==key):
            return 1
        elif(arr[middle]>key):
            end = middle - 1
        else:
            start = middle + 1

A = [7,2,4,3,5,7,8,9]
A.sort()
print(bSearch(A, len(A), 5))

# key = 4
# A = [7, 2, 4]
#
# print(search(A,3,4))
# print(find(A,3,8))