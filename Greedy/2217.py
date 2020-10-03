"""
백준 1931. 단어 수학
blog :
problem : https://www.acmicpc.net/problem/1339
"""
import sys

if __name__ == "__main__":

    N = int(sys.stdin.readline())

    ndict = {}
    for i in range(N):
        slist = input()
        position = 0
        sum = 0
        for s in reversed(slist):
            if s in list(ndict.keys()):
                sum = ndict.get(s) + pow(10, position)
                ndict.update({s: sum})
            else:
                ndict.update({s: pow(10, position)})
            position+=1
    res = sorted(ndict.items(), key=(lambda x: x[1]), reverse=True)

    num = 9
    result = 0
    for k, v in res:
        result = result + num * v
        num = num - 1

    print(result)



