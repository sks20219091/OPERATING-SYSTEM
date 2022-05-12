import os

r1,w1=os.pipe()
r2,w2=os.pipe()

pid=os.fork()

def vowel(st):
	i=0
	n=len(st)
	v=0
	for i in st:
		if(i=='a' or i=='A'or i=='e'or i=='E'or i=='i'or i=='I'or i=='o'or i=='O'or i=='u'or i=='U'):
			v=v+1
	const=n-v
	str3=str(v)+" & "+str(const)
	return str3
	

if pid>0:#p to c
	os.close(r1)
	w1=os.fdopen(w1,'w')
	string = input("Enter the string : ")
	w1.write(string)
	w1.close()
	
	#p recieving from c via pipe2
	os.close(w2)
	r2=os.fdopen(r2)
	str2=r2.read()
	print("The no. of vowel & consonant in string are  ",str2)
	r2.close()
	

else:	#c recieving from p via pipe1
	os.close(w1)
	r1=os.fdopen(r1)
	str1=r1.read()
	r1.close()
	
	result=vowel(str1)
	
	#c to p via pipe2
	os.close(r2)
	w2=os.fdopen(w2,'w')
	w2.write(result)
	w2.close()
	
