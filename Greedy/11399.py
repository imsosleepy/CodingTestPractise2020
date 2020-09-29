n = input()

list = list(map(int, input().split(" ")))
list.sort()
sum = 0
for i in range(int(n)):
    for j in range(i+1):
        sum = sum + list[j]

print(sum)