#재귀함수 이용
def r(x):
    if x<2 : return x
    return r(x-1)+r(x-2)

print(r(int(input())))