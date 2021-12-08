fname = input('enter file:')
if len(fname) < 1:
    fname = 'clown.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        print(w)
        if w in di:
            di[w] = di[w] + 1
            print("**Existing**")
        else:
            #initialize
            di[w] = 1
            print("**NEW**")
        print(w,di[w])