import sys

if __name__ =="__main__":
    T = int(sys.stdin.readline())

    for i in range(T):
        N = int(sys.stdin.readline())
        score = []
        count = 1
        for j in range(N):
           score.append(list(map(int, sys.stdin.readline().split())))

        score.sort()

        low_score = score[0][1]
        pass_list = []
        for j in range(N):
            if low_score >= score[j][1]:
                pass_list.append(score[j])

        for j in range(0,len(pass_list)):
            if low_score > pass_list[j][1]:
                count+=1
                low_score = pass_list[j][1]

        #print(pass_list)
        print(count)

