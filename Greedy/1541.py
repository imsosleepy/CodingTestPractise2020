"""
백준 1541. 잃어버린 괄호
blog :
problem : https://www.acmicpc.net/problem/1946
"""
import sys

if __name__ == "__main__":

    N = sys.stdin.readline().split("-")
    N = list(map(lambda s:s.strip(), N))
    sum = 0
    sum_list = []
    for i in range(0, len(N)):
        plus_list = str(N[i]).split("+")
        temp_sum = 0
        for j in range(len(plus_list)):
            temp_sum += int(plus_list[j])
        sum_list.append(temp_sum)
    sum = sum_list[0]
    for j in range(1, len(sum_list)):
        sum -= sum_list[j]

    print(sum)
