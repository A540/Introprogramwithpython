a = int(input('자연수 입력 : '))
if a <= 0 :
    print(a, '은(는) 자연수가 아닙니다.')
i = 1
s = 0
while i <= a/2:
    if a % i == 0:
        s += i
    i += 1
if s == a:
    print(a, '은(는) 완전수입니다.')
else:
    print(a, '은(는) 완전수가 아닙니다.')