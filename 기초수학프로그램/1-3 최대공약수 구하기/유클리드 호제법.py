a, b = map(int, input('비교할 두 수 입력 : ').split())
if a < b:
    a, b = b, a
while a % b != 0:
    c = a % b
    a, b = b, c
print('최대공약수 : ', b)