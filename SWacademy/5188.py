"""
SW Expert Academy 5188. 최소합
"""
import sys
from queue import Queue
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    a_map = [[0] * N for _ in range(N)]
    answer_map = [[11] * N for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    answer = 0

    for i in range(N):
        a_list = list(map(int, sys.stdin.readline().strip().split()))
        for j in range(len(a_list)):
            a_map[i][j] = a_list[j]
    print(a_map)

    q = Queue()

    q.put([0, 0])
    visited[0][0] = True

    while not q.empty():
        x, y = q.get()
        mx = [1, -1, 0, 0]
        my = [0, 0, 1, -1]

        for i in range(4):
            nx = x + mx[i]
            ny = y + my[i]

            if x < nx < N or y < ny < N:
                answer_map[nx][ny] = min(answer_map[nx][ny], a_map[x][y] + a_map[nx][ny])
                q.put([nx, ny])

    print(answer_map)




    result = "#" + str(test_case) + " " + str(answer)
    print(result)

    # ///////////////////////////////////////////////////////////////////////////////////
