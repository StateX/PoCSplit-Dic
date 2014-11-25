d1 = raw_input("Dame el archivo: ")

with open(d1,'r') as f:
    for line in f:
        for word in line.split():
           dic = open("dicslipt.txt","a+")
           dic.write(word + "\n")
           print word
    print "split done"   