list_data = list()
result = [[0] * 5 for i in range(5)]

for t in range(5):
    list_data += list(map(int,input().split()))
print(list_data)
list_data.sort()
print(list_data)

