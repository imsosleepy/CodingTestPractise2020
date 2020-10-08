"""
백준 1700. 멀티탭 스케줄링(-ing)
blog :
problem : https://www.acmicpc.net/problem/1700
"""
import sys

if __name__ == "__main__":

    n, k = map(int, sys.stdin.readline().strip().split())
    usage_list = list(map(int, sys.stdin.readline().strip().split()))

    plug = [0] * n
    count = 0

    for idx in range(len(usage_list)):
        # 현재 플러그에 꽂혀있는 장비라면 지나감
        if usage_list[idx] in plug:
            continue
        # 먼저 플러그 빈 곳이 있으면 꽂아준다
        if 0 in plug:
            for i, item in enumerate(plug):
                if item == 0:
                    plug[i] = usage_list[idx]
                    break
        # 빈 곳이 없으면
        else:
            # 꽂혀 있는 것들 중 앞으로 한번도 등장하지 않는 것을 가장 먼저 빼준다.
            is_pop = False
            for i, item in enumerate(plug):
                if item not in usage_list[idx:]:
                    plug[i] = usage_list[idx]
                    count+=1
                    is_pop = True
                    break
            # 모두 등장한다면 가장 나중에 등장하는 것을 가장 먼저 뽑아준다.
            # 전체리스트에 index j와 값 usage와 현재 플러그 item을 비교
            # item과 usage가 같으면 전체 리스트의 index를 저장
            if not is_pop:
                latest = 0
                latest_i = 0
                for i, item in enumerate(plug):
                    for j, usage in enumerate(usage_list[idx:]):
                        if item == usage:
                            if latest < j:
                                latest = j
                                latest_i = i
                                break
                plug[latest_i] = usage_list[idx]
                count += 1

    print(count)