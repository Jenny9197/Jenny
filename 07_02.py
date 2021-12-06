fhand = open('tesst.txt')
for line in fhand:
    print(line)

fhand = open('tesst.txt')
count = 0
for line in fhand:
    count = count+1
print('Line Count: ', count)

#read the file as whold
fhand = open('tesst.txt')
inp = fhand.read()
print(len(inp))
print(inp[:20])

#search the content of the file
fhand = open('mbox-short.txt')
for line in fhand:
    if line.startswith('From:'):
        print(line)
#input file name
fname = input('Enter the file name:  ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened: ', fname)
    quit()

count = 0
for line in fhand:
    if line.startswith('Subject:') :
        count = count + 1
print('There were', count, 'subject lines in', fname)

import re
hand = open('file name')
x = list()
for line in hand:
    y = re.findall('[0-9]+', line)
    x = x+y

sume = 0
for z in x:
    sum = sum + int(z)
print(sum)