N= int(input())

array = list(map(int, input().split()))

max = array[0]
min = array[0]

for i in range(1, N):
    if max < array[i]:
        max = array[i]
    if min > array[i]:
        min = array[i]

print(min, max)