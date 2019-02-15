a= list(map(int,input().split()))
cnt = [0]*10 #0부터 9까지

for i in range(6):
    cnt[a[i]] += 1
print(cnt)
time = 0
i = 0
tri = run = 0
while i < 10:
    if cnt[i] >= 3:
        cnt[i] -= 3
        tri += 1
    if i <= 7 and cnt[i]>=1 and cnt[i+1]>=1 and cnt[i+2]>=1:
        cnt[i] -= 1
        cnt[i+1] -= 1
        cnt[i+2] -= 1
        run += 1
    i += 1
print(run)
if run + tri == 2:
    print("babygin")
else:
    print("No")

