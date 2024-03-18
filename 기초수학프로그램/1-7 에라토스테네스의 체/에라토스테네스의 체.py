n = 0
while n < 2:
    n = int(input('자연수 N 입력 : '))
    if n < 2:
        print(n, '은(는) 2이상의 자연수가 아닙니다.')
i = 0
a = []
while i <= n:
    a.append(i)
    i += 1
a[1] = 0
i = 2
while i < n / 2:
    j = 2
    while i * j <= n:
        a[i * j] = 0
        j += 1
    i += 1
for k in a:
    if k != 0:
        print(k, end=' ')
