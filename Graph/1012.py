"""
백준 1012. 유기농 배추
blog :
problem : https://www.acmicpc.net/problem/1012
"""

import sys
from queue import Queue

if __name__ == "__main__":
    t = sys.stdin.readline()
    m, n, k = map(int, sys.stdin.readline().strip().split())
    # print(m, n, k)
    blist = [[0] * n for _ in range(m)]

    print(blist)