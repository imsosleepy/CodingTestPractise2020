"""
백준 1449. 수리공 항승
blog :
problem : https://www.acmicpc.net/problem/1449
"""
import sys

if __name__ == "__main__":

    n, l = map(int, sys.stdin.readline().strip().split())
    holes = list(map(int, sys.stdin.readline().strip().split()))

    holes.sort()
    # 정렬 후 맨 앞의 테이프가 커버할 수 있는 공간을 미리 구해둔다.
    # 여유공간으로 0.5를 두는 걸 유의해서 하면 됨
    coverage = holes[0] + l - 0.5
    count = 1
    # 구멍난 공간이 커버할 수 있는 범위를 넘어가면 새 테이프를 붙이고
    # 그 테이프가 커버할 수 있는 공간으로 치환해준다.
    # 그리고 테이프 개수 하나 추가
    for i in range(1, n):
        if coverage < holes[i]:
            coverage = holes[i] + l - 0.5
            count += 1

    print(count)







