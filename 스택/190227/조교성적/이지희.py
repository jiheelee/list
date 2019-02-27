import sys
sys.stdin = open('input.txt','r')

result_list = ["A+","A0","A-","B+","B0","B-","C+","C0","C-","D0"]
N, K = map(int,input().split())
score = []
for n in range(N):
    A, B, C = map(int,input().split())
    result = 0.35 * A + 0.45 * B + 0.2 * C
    score.append(result)
score.sort()
print(score)

