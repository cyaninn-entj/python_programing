inStr = input("문자열을 입력하세요 :")
outStr = ""

upper,lower,digit,hangul,etc = [0]*5

for i in inStr:
    if ord('a') <= ord(i) <= ord('z'):
        lower += 1
    elif ord('A') <= ord(i) <= ord('Z'):
        upper += 1
    elif ord('가') <= ord(i) <= ord('힣'):
        hangul += 1
    elif ord('0') <= ord(i) <= ord('9'):
        digit += 1
    else:
        etc += 1

print("대문자:%d,소문자:%d,숫자:%d,한글:%d,기타:%d" % (upper,lower,digit,hangul,etc))