N, K = map(int, input().split())

coin = []
for i in range(N):
    c = int(input())
    coin.append(c)
count = 0
while(True):
    if K == 0:
        break;
    for i in range(N,0,-1):
        if int(K/coin[i-1]) == 0:
            continue
        else:
            count = count + int(K / coin[i-1])
            K = K % coin[i-1]
print(count)

# 가장 큰 동전부터 처리하면 된다.
