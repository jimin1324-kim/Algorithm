first, second, third = map(int, input().split()) # 띄어쓰기를 기준으로 나눠 입력받음

if first == second and second == third:
    print(10000 + first*1000)
elif first == second or second == third or first == third:
    if first == second:
        print(1000+first*100)
    else:
        print(1000+third*100)
else:
    print(max(first, second, third)*100)