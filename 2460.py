# 4. 지능형 기차 2
# 도중 기차 안에 사람이 가장 많을 때의 사람 수를 계산하려고 한다.
# 역에서 기차에 탈 때, 내릴 사람이 모두 내린 후에 기차에 탄다고 가정한다.

def solution(outnum, innum):
    answer = True
    max = 0
    people = 0
    for i in range(0, 10):
        people = people - int(outnum[i]) + int(innum[i])
        if people > max :
            max = people
    print (max)
    return True


if __name__ == '__main__':
    outnum = [0]*10
    innum = [0] * 10
    for i in range(0, 10) :
        num = input().split(' ')
        outnum[i] = int(num[0])
        innum[i] = int(num[1])
    solution(outnum, innum)

