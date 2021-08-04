# 5. 피보나치 수 5
# 첫째 줄에 n이 주어진다. n은 20보다 작거나 같은 자연수 또는 0이다.
# n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.

pipo = [0]*21
num = int(input())
pipo[0]=0
pipo[1]=1
for i in range(2, 21):
    pipo[i] = int(pipo[i-2]) + int(pipo[i-1])
print(pipo[num])

