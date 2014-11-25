
def abrirguardar(txt):
	with open(txt,'r') as f:
		for line in f:
			for word in line.split():
				if word + "\n" in comp:
					pass
				else: 	
					dic.write(word+"\n")
		print "Done"   

while True: 
	d1 = raw_input("Dame el archivo: ")
	dic = open("dicslipt.txt","a+")
	comp =[]
	for word in dic:
		comp.append(word) 
	abrirguardar(d1)    