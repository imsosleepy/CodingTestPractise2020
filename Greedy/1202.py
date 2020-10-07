"""
백준 1202. 보석 도둑
blog :
problem : https://www.acmicpc.net/problem/1946
"""

'''
가장 처음에 떠올렸던 방법인 이중 for문으로 처리하는 방법
당연히 시간 초과가 났다. 애초에 log(N^^2)의 시간 복잡도가 나오는데, 최대 크기가 1000000이라
해볼 이유조차 없었는데.... list에서 pop하는 과정을 넣어서 횟수가 줄지 않을까 했는데
최악의 경우가 예시로 있었나보다
아래는 수동으로 입력 가능한 몇가지 예제는 통과하나 제출 했을시 타임오버가 난다.
'''
# import sys
#
# if __name__ == "__main__":
#
#     N, K = map(int, sys.stdin.readline().strip().split())
#
#     jewel = []
#     for i in range(N):
#         M, V = map(int, sys.stdin.readline().strip().split())
#         jewel.append((M, V))
#
#     bag = []
#     for i in range(K):
#         C = int(sys.stdin.readline().strip())
#         bag.append(C)
#
#     jewel = sorted(jewel, key=lambda x: x[0])
#     bag.sort()
#
#     answer = []
#     is_in = False
#     for c in bag:
#         vmax = 0
#         mmin = 100000001
#
#         for m, v in jewel:
#             # 가방이 들 수 있는 무게가 보석보다 무게보다 클 때
#             if c >= m:
#                 # 가장 큰 가치를 가진게 들어가야 함
#                 if v > vmax:
#                     vmax = v
#                     mmin = m
#                     is_in = True
#
#         answer.append(vmax)
#
#         if is_in:
#             jewel.remove((mmin, vmax))
#
#     print(sum(answer))

'''
힙을 쓰거나 우선순위 큐를 써서 시간복잡도를 줄여야 한다고 한다.
파이썬에서 제공하는 힙은 최소 힙임(힙에 리스트를 입력하면 오름차순으로 자동정렬)
최대 힙으로 사용하기 위해서 음수를 곱하는 트릭을 씀
힙의 시간복잡도는 nlog(n) 수준이고, 최적이라면 n으로 떨어진다고 한다.
참고 : https://peisea0830.tistory.com/9
'''

import sys, heapq

if __name__ == "__main__":

    N, K = map(int, sys.stdin.readline().strip().split())

    jewel = []
    for i in range(N):
        M, V = map(int, sys.stdin.readline().strip().split())
        jewel.append([M, V])

    bags = []
    for i in range(K):
        C = int(sys.stdin.readline().strip())
        bags.append([C, -1]) # 가방임을 알려주기 위한 -1

    jewel_bags = jewel + bags
    jewel_bags = sorted(jewel_bags, key=lambda x: x[0])

    max_list = []
    answer = 0
    for item in jewel_bags:
        if item[1] != -1:
            heapq.heappush(max_list, (-1 * item[1], item[1]))
        else:
            if max_list:
                answer = answer + heapq.heappop(max_list)[1]
    print(answer)




