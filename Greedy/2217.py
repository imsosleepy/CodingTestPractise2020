"""
백준 1931. 로프
blog :
problem : https://www.acmicpc.net/problem/2217
"""
import sys

if __name__ == "__main__":

    N = int(sys.stdin.readline())

    rope = []
    for i in range(N):
        rope.append(int(sys.stdin.readline()))

    rope.sort()
    max_power = 0
    for i in range(N):
        sum = rope[i] * (N-i)
        max_power = max(sum, max_power)
    print(max_power)