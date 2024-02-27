while 1:
    a = int(input('자연수 입력 : '))
    if a <= 0 :
        print(a, '은(는) 자연수가 아닙니다.')
    else:
        break

i = 1
print(a, '의 모든 약수 : ', end=' ')
while i <= a/2:
    if a % i == 0:
        print(i, end=' ')
    i += 1
print(a)