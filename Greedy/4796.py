"""
백준 4796. 캠핑
blog :
problem : https://www.acmicpc.net/problem/4796
"""
import sys

if __name__ == "__main__":
    count = 0
    while True:
        count+=1
        answer = 0
        L, P, V = map(int, sys.stdin.readline().strip().split())
        if P == 0 and L == 0 and V == 0:
            break

        q = int(V / P) * L
        r = int(V % P)
        if r > L:
            r = L
        answer = q + r
        print("Case " + str(count) + ": " + str(answer))