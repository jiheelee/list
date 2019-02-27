def find(l,r):
    if l==r:
        return l
    else:
        r1 = find(l,r//2+1)
        r2 = find()