def isPrime(a):
    isp = True
    i = 2
    while isp == True and i <= a / 2:
        if a % i == 0:
            isp = False
        i += 1
    if isp == True:
        return a
    else:
        return False
n = False
while n == False:
    a = int(input('2이상의 자연수 입력 : '))
    if a < 2:
        print(a, '은(는) 2 이상의 자연수가 아닙니다')
    else:
        n = True

for i in range(2, a):
    p = isPrime(i)
    if p != False:
        print(p, end=' ')