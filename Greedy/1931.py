"""
백준 1931. 회의실배정
blog : https://blog.naver.com/kimdongha15/222103174591
problem : https://www.acmicpc.net/problem/1931
"""
import sys

def greedy(meeting):
    meeting_count = 0
    start_time = 0

    for time in meeting:
        if time[0] >= start_time:
            start_time = time[1]
            meeting_count += 1
    return meeting_count

if __name__ =="__main__":
    N = int(sys.stdin.readline())
    input_list = []
    count = 0
    for i in range(N):
        input_list.append(list(map(int, sys.stdin.readline().split())))
    meeting = []
    meeting = sorted(input_list, key=lambda x: x[0])
    meeting = sorted(meeting, key=lambda x: x[1])

    print(greedy(input_list))

# 정렬이 제일 중요한 문제였다
# 제대로 된 정렬 이후에 그리디 알고리즘으로 해결할 수 있음
# https://daimhada.tistory.com/38 블로그 참고

