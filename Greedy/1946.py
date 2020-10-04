"""
백준 1946. 신입사원
blog :
problem : https://www.acmicpc.net/problem/1946
"""

import sys

if __name__ =="__main__":
    T = int(sys.stdin.readline())

    for i in range(T):
        N = int(sys.stdin.readline())
        score = []
        count = 1
        for j in range(N):
           score.append(list(map(int, sys.stdin.readline().strip().split())))

        score.sort()

        low_score = score[0][1]

        for j in range(0,len(score)):
            if low_score < score[j][1]:
                continue
            if low_score > score[j][1]:
                count+=1
                low_score = score[j][1]

        print(count)

