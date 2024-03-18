def encipher(p, k):
    a = ord(p)
    if a == 32:
        a = 96
    t = a + k
    if t > 122:
        t = t % 122
    if t < 27:
        t += 95
    if t == 96:
        t = 32
    return chr(t)


p = input("평문 입력 :")
k = int(input("K 값 입력 :"))
n = len(p)
c = ""
for i in range(n):
    c = c + encipher(p[i], k)
print(f"암호문 출력 : [{c}]")