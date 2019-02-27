cnt = 0
def f(n, k):
    global cnt
    if(n==k):
        print(p)
        cnt += 1


    else:
        for i in range(1, k+1):
            p[n] = i
            f(n+1, k)

K = 3
p = [0] * K
f(0, K)
print(cnt)