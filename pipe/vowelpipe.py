import os

r1,w1=os.pipe() #P TO C
r2,w2=os.pipe() #C TO P

pid=os.fork()

def vowel(st):
	i=0
	c=0
	n=len(st)
	for i in st:
		if(i=='a' or i=='A' or i=='e' or i=='E' or i=='i' or i=='I' or i=='o' or i=='O' or i=='U' or i=='u'):
			c=c+1
		
	const = n-c
	str3=str(c)+" & "+str(const)
	return str3		
		

if pid>0:
	print("P to C")
	os.close(r1)
	w1=os.fdopen(w1,'w')
	string=input("Enter the string ")
	w1.write(string)
	w1.close()
	
	print("p recieving from c via pipe2")
	os.close(w2)
	r2=os.fdopen(r2)
	str2=r2.read()
	print("The number of vowel & consonant in the string are ",str2)
	r2.close() 	
	
	


else:	
	
	os.close(w1)
	
	r1=os.fdopen(r1)
	print("c recieving from P via pipe 1")
	str1=r1.read()
	r1.close()
	
	print("count no of vowel ")
	count=vowel(str1)
	
	print("c to p via pipe2")
	os.close(r2)
	w2=os.fdopen(w2,'w')
	w2.write(count)
	w2.close()
	
