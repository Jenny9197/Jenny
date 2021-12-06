fopen = open('mbox-short.txt')
for line in fopen:
    ly = line.rstrip()
    print(ly.upper())