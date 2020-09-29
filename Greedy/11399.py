n = input()

list = list(map(int, input().split(" ")))
list.sort()
sum = 0
for i in range(int(n)):
    for j in range(i+1):
        sum = sum + list[j]

print(sum)

# 정렬 후 가장 작은 것부터 순차적으로 합을 구한다.
