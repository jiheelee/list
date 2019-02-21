N = int(input())
M = int(input())
secret_code = ""
num_list = ['0001101','0011001','0010011','0111101','0100011','0110001','0101111','0111011','0110111','0001011']
for n in range(N):
    k =  str(input())
    if "1" in k:
        secret_code += k
        break
for idx, val in enumerate(num_list):

    result = secret_code.replace(val,str(idx))

print(secret_code)

