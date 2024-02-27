print('정수 a, b, c, d 입력 : ')
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
d = int(input('d = '))
print('정렬 전 : ', a, b, c, d)
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if c > d:
    c, d = d, c
# 가장 큰 수를 d로 보냄
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
# 두 번째로 큰 수를 c로 보냄
if a > b:
    a, b = b, a
# 세 번째로 큰 수를 b로 보냄, a는 자연히 가장 작은 수
print('정렬 후 : ', a, b, c, d)