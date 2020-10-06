"""
백준 2437. 저울
blog :
problem : https://www.acmicpc.net/problem/2437
"""

import sys
from itertools import combinations
if __name__ == "__main__":
    N = int(sys.stdin.readline())
    weight_list = []
    weight_list = list(map(int, sys.stdin.readline().strip().split()))
    weight_list.sort()

    sum = 1
    answer = 0
    # 처음에 1이 없다면, 1을 만들 수 없음
    if weight_list[0] != 1:
        answer = 1
    # 다음 무게 추가 누적합+1보다 클 경우, 누적합+1의 무게를 만들 수 없다.
    # sum 까지의 모든 무게는 만들 수 있기 때문에,
    # 추가적으로 들어오는 추의 무게가 다음 목표 무게보다 작다면,
    # 이전 누적합+다음에 들어오는 무게추의 무게까지는 만들 수 있음
    # 그러나 새로 들어오는 추의 무게가 다음 목표 숫자보다 큰 수가 들어오게되면
    # 그 무게추+누적합과 누적합 사이의 무게의 공백이 생긴다.
    # 때문에 만들 수 없는 가장 작은 무게는 현재까지 만들 수 있었던 무게의 +1이 된다.
    else:
        for i in range(1, N):
            if weight_list[i] > sum + 1:
                answer = sum + 1
                break
            sum = sum + weight_list[i]

        answer = sum + 1

    print(answer)

