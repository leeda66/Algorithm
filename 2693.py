#8. N번째 큰 수

num = int(input())
for i in range(num):
    list = list(map(int, input().split()))
    list.sort()
    print(list[-3])
