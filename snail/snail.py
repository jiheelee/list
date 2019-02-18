
snail_list = []

for i in range(5):
    arr = list(map(int,input().split()))
    snail_list.extend(arr)
print(snail_list)
for i in range(24):
    minIdx = i
    for j in range(1,25):
        if (snail_list[minIdx] > snail_list[j]):
            minIdx = j
        snail_list[i], snail_list[minIdx] = snail_list[minIdx], snail_list[i]

print(snail_list)