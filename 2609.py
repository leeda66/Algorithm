#7. 최대공약수, 최소공배수
num=input().split(' ')
a=int(num[0])
b=int(num[1])

def fun(s, b):
    min = 0
    max = 0
    # 최대공약수
    for i in range(b+1, 1, -1):
        if s == 1:
            max=1
        elif(b%i==0 and s%i==0):
            max=i
            break
        else:
            max=1
    # 최소공배수
    if b%s==0:
        min = b
    else :
        for i in range(1, s+1):
            if((b*i)%s==0):
                min=b*i
                break
    print(max)
    print(min)


if a>b:
    fun(b,a)

elif b>a:
    fun(a,b)

else :
    print(a)
    print(b)