def f(n, k):
    if (n==k):
        for i in range(k):
            if(b[i]==1):
                print(a[i],end =" ")
        print()
        return
    else:
        b[n] = 0
        f(n+1,k)
        b[n] = 1
        f(n+1, k)
a = [10,20,30]
K = 3
b = [0]*K
f(0,K)