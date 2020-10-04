"""
백준 1744. 수 묶기
blog :
problem : https://www.acmicpc.net/problem/1946
"""

import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    positive_list = []
    negative_list = []
    zero = 0
    # 양수, 음수, 0을 각각 리스트에 저장
    for i in range(N):
        num = int(sys.stdin.readline().strip())
        if num > 0:
            positive_list.append(num)
        elif num == 0:
            zero += 1
        elif num < 0:
            negative_list.append(num)

    result = []
    positive_list.sort(reverse=True) # 오름 차순 정렬
    negative_list.sort() # 내림 차순 정렬
    # 양수 리스트 처리
    for i in range(0, len(positive_list) - 1, 2):
        # 묶음에 1이 포함되있을 때는 더하는게 곱하는 것보다 크다(묶지 않는다)
        if positive_list[i] == 1 or positive_list[i+1] == 1:
            result.append(positive_list[i] + positive_list[i + 1])
            continue
        # 이외의 조건에선 그냥 곱해서 결과 리스트에 삽입
        result.append(positive_list[i] * positive_list[i+1])
    # 음수 리스트 처리
    for i in range(0, len(negative_list) - 1, 2):
        # 음수는 그냥 곱해서 결과리스트에 삽입
        result.append(negative_list[i] * negative_list[i+1])

    # 각 리스트의 크기가 짝수가 아닐 때의 처리
    # 음수 리스트에 한개가 남았고, 전체 리스트에 0이 포함되어 있을 때
    if len(negative_list) % 2 != 0 and zero != 0:
        # 남은 숫자는 0을 곱해서 0으로 만드는게 이득
        result.append(0)
    # 음수 리스트에 한개가 남았고, 전체 리스트에 0이 포함되어 있지 않을 때
    elif len(negative_list) % 2 != 0:
        # 그냥 결과 리스트에 넣어준다.
        result.append(negative_list[-1])
    # 양수 리스트에 한개가 남았을 때는 그냥 결과리스트에 넣어준다.
    if len(positive_list) % 2 != 0:
        result.append(positive_list[-1])

    # 결과 리스트의 합을 출력
    print(sum(result))
