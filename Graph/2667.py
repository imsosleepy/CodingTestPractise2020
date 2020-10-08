"""
백준 2667. 미로 탐색
blog :
problem : https://www.acmicpc.net/problem/2667
"""
import sys
from queue import Queue


def bfs(start, end, matrix, visited):
    count = 1
    visited[start][end] = True
    q = Queue()
    q.put([start, end])
    size = len(matrix)
    while not q.empty():
        x, y = q.get()
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < size and 0 <= ny < size and not visited[nx][ny] and matrix[nx][ny] == '1':
                count += 1
                visited[nx][ny] = True
                q.put([nx, ny])

    return count


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    matrix = [[0] * n for _ in range(n)]
    visited = [[False] * n for _ in range(n)]

    for x in range(n):
        row = sys.stdin.readline().strip()
        for y in range(n):
            matrix[x][y] = row[y]

    answer = []
    for x in range(n):
        for y in range(n):
            if not visited[x][y] and matrix[x][y] == '1':
                answer.append(bfs(x, y, matrix, visited))

    answer.sort()
    print(len(answer))
    for item in answer:
        print(item)



