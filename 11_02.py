import re
x = "My 2 favourite numbers are 19 and 42"
y = re.findall('[0-9]+',x)
print(y)
#find out the numbers from x statement
#['2','19','42]

import re
x = "My 2 favourite numbers are 19 and 42"
y = re.findall('[AEIOU]+',x)
print(y)
#find out the pattern of aeiou but there is no pattern
#so printout only blank list

import re
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)
#'^F.+:' find this pattern! but the longest one
#Greedy pattern

import re
x = 'From: Using the : character'
y = re.findall('^F.+?:', x)
print(y)
#non-greedy pattern because of adding '?'

x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'

y = re.findall('\S+@\S+',x)
print(y)

# ['stephen.marquard@uct.ac.za’]
#@에 해당하는 앞 뒤를 출력

x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('^From (\S+@\S+)',x)
print(y)

# ['stephen.marquard@uct.ac.za']
#from 으로 시작하는 문자열 출력