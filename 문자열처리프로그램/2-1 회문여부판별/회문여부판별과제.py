def isPalindrome(s):
    a = ""
    i = 0
    j = len(s) - 1
    while i <= j:
        if s[i].isalpha():
            a += s[i]
            i += 1
        else:
            i += 1

    a = a.lower()
    print("변환된 문자열 :", a)
    while i < j:
        if a[i] != a[j]:
            return False
        else:
            i += 1
            j -= 1
    return True


s = input("문자열 입력 :") 
b = isPalindrome(s)
if b:
    print("회문입니다.")
else:
    print("회문이 아닙니다.")