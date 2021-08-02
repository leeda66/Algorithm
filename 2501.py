# 1. 약수 구하기

def solution(num, k):
    answer = True
    result = [0]*num
    idx = 0;
    for i in range (1, num+1):
        if num % i == 0:
            result[idx] = i
            idx += 1
    #print(result)
    print(result[k-1])
    return True


if __name__ == '__main__':
    num = input().split(' ')
    num1 = num[0]
    num2 = num[1]
    solution(int(num1), int(num2))


