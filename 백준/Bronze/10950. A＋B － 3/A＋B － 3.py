T = int(input())
As = []
Bs = []

for i in range(1, T+1):
    A, B = map(int, input().split())
    As.append(A)
    Bs.append(B)

for i in range(1, T+1):
    print(As[i-1]+Bs[i-1])