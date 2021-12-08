#regular expressions #1
#re.search()
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.find('From: ')>=0:
        print(line)

import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line):
        print(line)
#second method
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.startswith('From: '):
        print(line)

import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)

import re
hand = open('mbox-short.txt')
temp = re.findall(r'\d+', test_string)
res = list(map(int, temp))
print(str(res))
#summary
#^  라인의 처음을 매칭

#$ 라인의 끝을 매칭

#. 임의의 문자를 매칭(와일드카드)

#\s 공백문자를 매칭

#\S 공백이 아닌 문자를 매칭

#* 바로 앞선 문자에 적용되고 0혹은 그 이상의 앞선 문자와 매칭을표기함.

#* ?  바로 앞선 문자에 적용되고 0 혹은 그 이상의 앞선 문자와 매칭을 탐욕적이지 않은 방식으로 표기함.        바로

#+    바로 앞선 문자에 적용되고 1 혹은 그 이상의 앞선 문자와 매칭을 표기함
#+?   바로 앞선 문자에 적용되고 1 혹은 그 이상의 앞선 문자와 매칭을 탐욕적이지 않은 방식으로 표기함.
#[aeiou] 명세된 집합 문자에 존재하는 단일 문자와 매칭. “a”, “e”, “i”, “o”, “u” 문자만 매칭되는 예제
#[a-z0-9]  - 기호로 문자 범위를 명세할 수 있다. 소문자이거나 숫자인 단일 문자만 매칭되는 예제
#( ) 괄호가 정규표현식에 추가될 때, 매칭을 무시한다. 하지만 findall()을 사용 할 때 전체 문자열보다 매칭된 문자열의 상세한 부속
#문자열을 추출할 수 있게 한다.

#find()함수는 'From:'의 위치가 문자열 내부에서 어디에 위치하는지 확인할 수 있습니다.
#'From:'이 line내에 존재할 시에 line에서의 위치를 알려주고
#존재하지 않을 시에 -1을 반환해줍니다.
#따라서 line.find('From:')==-1이 된다면 'From:'이 line내에 위치하지 않음을 의미하고
#line.find('From:')>=0이 된다면 line내의 어딘가에 존재함을 알 수 있겠죠
