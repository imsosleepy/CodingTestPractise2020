"""
SW Expert Academy 5186. 이진수2
"""

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    num = float(input())
    answer = ''
    for n in range(-1,-13,-1):
        if num == 0:
            break

        if num - float(pow(2, n)) >= 0:
            answer = answer + '1'
            num = num - float(pow(2, n))
        else:
            answer = answer + '0'

    if num > 0:
        answer = 'overflow'

    result = "#" + str(test_case) + " " + answer
    print(result)

    # ///////////////////////////////////////////////////////////////////////////////////
