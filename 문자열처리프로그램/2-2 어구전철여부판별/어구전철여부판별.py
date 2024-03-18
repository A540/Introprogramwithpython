def Clearing(s):
    s_c = ""
    for i in range(len(s)):
        if s[i].isalpha():
            s_c += s[i]
    return s_c

def listing(s):
    n = len(s)
    lt = []
    for i in range(n):
        lt.append(s[i])
    return lt


def isAnagram(s1, s2):
    s1 = Clearing(s1)
    s2 = Clearing(s2)
    n1 = len(s1)
    n2 = len(s2)
    if n1 != n2:
        return False
    list1 = listing(s1)
    list2 = listing(s2)
    list1.sort()
    list2.sort()
    i = 0
    while i < n1:
        if list1[i] != list2[i]:
            return False
        i += 1
    return True


s1 = input("첫 번째 문자열 입력: ")
s2 = input("두 번째 문자열 입력: ")
if isAnagram(s1, s2):
    print("어구 전철 입니다.")
else:
    print("어구 전철이 아닙니다.")