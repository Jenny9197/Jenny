fname = input('enter file:')
if len(fname) < 1:
    fname = 'clown.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        #first method
        #oldcount = di.get(w,0)
        #print(w,'old',oldcount)
        #newcount = oldcount+1
        #di[w] = newcount
        #second method
        di[w] = di.get(w,0) + 1
        #print(w,'new',newcount)
print(di)

#now we want to find the most common word
largest = -1
theword = None
for k,v in di.items():
    print(k,v)
    if v > largest:
        largest = v
        theword = k #cature the key that was largest
print('DONE',theword, largest)