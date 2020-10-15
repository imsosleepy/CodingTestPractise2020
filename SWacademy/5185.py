"""
SW Expert Academy 5185. 이진수
"""

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    l, p = map(str, input().split())
    answer = ''
    for num in p:
        cvt = bin(int(num, 16))[2:]
        if len(cvt) < 4:
            for _ in range(4 - len(cvt)):
                cvt = '0' + cvt
        answer = answer + cvt

    result = "#" + str(test_case) + " " + answer
    print(result)

    # ///////////////////////////////////////////////////////////////////////////////////
