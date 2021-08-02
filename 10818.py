# 3. 최소, 최대

def solution(n, list):
    answer = True
    min = 1000000
    max = -1000000
    for i in range (0, n):
        value = int(list[i])
        if(value < min) :
            min = value
        if(value > max) :
            max = value
    print(min, max)
    return True


if __name__ == '__main__':
    num1 = input()
    num2 = []
    num2 = input().split(' ')
    solution(int(num1), num2)
