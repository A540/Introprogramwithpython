while 1:
    n = int(input('N 입력 : '))
    if n <= 2:
        print('N은 2보다 큰 자연수여야 합니다.')
    else:
        break
for a in range(2, n):
    i = 1
    s = 0
    while i <= a / 2:
        if a % i == 0:
            s += i
        i += 1
    if s == a:
        print(a, end=' ')