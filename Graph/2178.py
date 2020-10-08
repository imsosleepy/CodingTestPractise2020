"""
백준 2178. 미로 탐색
blog :
problem : https://www.acmicpc.net/problem/2178
"""
import sys
from queue import Queue

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().strip().split())
    matrix = [[0] * m for _ in range(n)]
    # visited list를 만들어서 방문체크를 하면 타임아웃이 난다.
    # track은 결과 체크 용으로 만들었는데 두개의 list가 추가되면 time out!
    # track = [[0] * m for _ in range(n)]
    # visited = [[False] * m for _ in range(n)]

    for x in range(n):
        row = sys.stdin.readline().strip()
        for y in range(m):
            matrix[x][y] = int(row[y])

    q = Queue()
    q.put([0, 0])
    while not q.empty():
        x, y = q.get()
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 1:
                q.put([nx, ny])
                matrix[nx][ny] = matrix[x][y] + 1

    print(matrix[n-1][m-1])
