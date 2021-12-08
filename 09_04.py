fname = input('Enter file: ')
if len(fname) < 1:
    fname = 'clown.txt'
#recognize as a basic value
hand = open(fname)

for line in hand:
    line = line.rstrip()
    print(line)
    wds = line.split()
    print(wds)
    for w in wds:
        dic[w] = dic.get(w,0) + 1

largest = -1
theword = None
for k,v in dic.items():
    print(k,v)
    if v > largest:
        largest = v
        theword = k
print('done',theword, largest)
