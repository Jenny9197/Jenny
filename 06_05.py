str = 'X-DSPM-Confidence: 0.8475'

ipos = str.find(':')
piece = str[ipos+2:]
value = float(piece)
print(value)

words = 'Connect Foundation'

if 'F' in words:
    word = words.lower()
    nword = word.replace(' ', '&')
else:
    print(words)
print(nword)

== == == == == == == == == == == == == == == == == == == == == == == == =
# words = 'Connect Foundation'



# if 'F' in words:
#     words.lower()
#     word[7] = '&'
# else:
#     print(words)
# print(words)
# TypeError: 'str' object does not support item assignment



# 일단 words.lower()도 출력이 안될것입니다.
# words.lower()를 하면 소문자로 바꾼 그값을 어느 변수에 저장해야되는데,
# 그냥 바꿔만 줬지, 변수를 만들어 저장을 해주지 않았기때문에
# 출력은 되지않을것입니다.



# 일단, 오류나는 부분인 word[7]='&'을 제거하고 출력하더라도
# Connect Foundation 이 값으로 출력될 것입니다.



# 문자열 안의 값을 직접 바꿀수는 없고,
# 문자열안의 인덱스 요소를 바꾸려면 replace()함수를 사용해서 바꿔주야합니다.

words = 'Connect Foundation'

if 'F' in words :
    b = words.lower()
    c = b.replace(' ','&')
else :
    print(words)
print(c)