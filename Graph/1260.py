"""
백준 1260. bfs와 dfs
blog :
problem : https://www.acmicpc.net/problem/1260
"""
import sys
from queue import Queue


def bfs(start, matrix, visited):
    visited[start] = True
    q = Queue()
    q.put(start)

    while not q.empty():
        t = q.get()
        print(str(t), end=' ')
        for i in range(1, len(matrix)):
            if matrix[t][i] == 1 and visited[i] is False:
                q.put(i)
                visited[i] = True



def dfs(start, matrix, visited):
    visited[start] = True
    print(str(start), end=' ')
    for i in range(1, len(matrix)):
        if matrix[start][i] == 1 and visited[i] is False:
            dfs(i, matrix, visited)

if __name__ == "__main__":
    n, m, v = map(int, sys.stdin.readline().strip().split())
    matrix = [[0] * (n + 1) for _ in range(n+1)]
    # 아래와 같다
    # matrix = []
    # for _ in range(n + 1):
    #    matrix.append([0] * (n + 1))
    visited = [False] * (n + 1)

    for _ in range(m):
        s, e = map(int, sys.stdin.readline().strip().split())
        matrix[s][e] = matrix[e][s] = 1

    dfs(v, matrix, visited)
    print()
    visited = [False] * (n + 1)
    bfs(v, matrix, visited)

