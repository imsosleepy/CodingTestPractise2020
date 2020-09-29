n = int(input())

result = 0
while(True):
    temp = n
    # 5로 나누어 떨어졌을 때
    # 몫이 0 일때랑 0이 아닐 때로 나뉨
    if temp % 5 == 0:
        result = int(temp/5)
        break
    elif temp % 5 != 0 and int(temp/5) == 0:
        if temp % 3 == 0:
            result = result + 1
            break
        elif temp % 3 != 0:
            result = -1
            break
    # 5로 나누어 떨어지지 않았을 때
    else:
        # 3으로 나눈다.
        # 나머지가 0일 때
        if (temp % 5) % 3 == 0:
            result = result + int(temp/5) + 1
            break
        # 나머지가 0이 아닐 때
        else:
            n = n - 3
            result = result + 1

print(result)