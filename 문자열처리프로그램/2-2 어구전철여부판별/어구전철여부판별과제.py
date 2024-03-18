def perm(a, i, n, lt):
    if i == n - 1:
        s_c = ""
        for k in range(n):
            # print(a[k], end='')
            s_c += a[k]
        lt.append(s_c)
    else:
        for j in range(i, n):
            a[i], a[j] = a[j], a[i]
            perm(a, i + 1, n, lt)
            a[i], a[j] = a[j], a[i]


s1 = input('첫 번째 문자열 입력: ')
s2 = input('두 번째 문자열 입력: ')
N = len(s1)
s = []
for i in range(N):
    s.append(s1[i])
lt = []
perm(s, 0, N, lt)
t = False
for i in lt:
    if i == s2:
        t = True
    else:
        t = False
if t == True:print('어구 전철 입니다.')
else: print('어구 전철이 아닙니다.')