a = int(input('자연수 a 입력 : '))
isPrime = True
i = 2
while isPrime == True and i <= a/2:
    if a % i == 0:
        isPrime = False
    i += 1
if isPrime == True:
    print('a는 소수입니다')
else:
    print('a는 소수가 아닙니다')