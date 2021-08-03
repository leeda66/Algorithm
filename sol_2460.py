import sys

maxpass = 0
current = 0

for i in range(10):
    A,B = map(int, sys.stdin.readline().split())
    current -= A
    current += B
    if maxpass<current: maxpass = current
print(maxpass)