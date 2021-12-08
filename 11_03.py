#double split pattern
words = line.split()
email = words[i]
pieces = email.split('@')
print(pieces[1])
shong@ualberta.ca
['shong','ualberta.ca']
'ualberta.ca'

import re
hand = open('mbox.short.txt')
numlst = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1:
        num = float(stuff[0])
        numlst.append(num)
    print('Maximum:', max(numlst))