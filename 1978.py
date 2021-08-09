num = int(input())
nums = list(map(int, input().split()))
sosu = 0

for i in range (num) :
    value = nums[i]
    if value ==2 or value ==3:
        sosu+=1
        continue

    for j in range (2, value):
        if value % j == 0:
            break
        else:
            sosu += 1

print(sosu)