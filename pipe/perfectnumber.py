import os
import math

r1,w1=os.pipe()
r2,w2=os.pipe()

pid=os.fork()

def sumofprime(string):
	numberlist=string.split()
	i=0
	n=len(numberlist)
	sum=0
	while i<n:
		number=int(numberlist[i])
		x=int(math.sqrt(number))
		if x*x==number:
			sum=sum+number
		i=i+1
			
	return str(sum)		
		
	

if pid>0: 
	#P TO C VIA PIPE1
	os.close(r1)
	w1=os.fdopen(w1,'w')
	n=int(input("Enter the numbers of elements"))
	i=0
	str1=""
	while i<n:
		x=int(input("Enter the number: "))
		str1=str1+" "+str(x)
		i=i+1
	w1.write(str1)
	w1.close()
	
	#p recieving from c via pipe2
	os.close(w2)
	r2=os.fdopen(r2)
	str3=r2.read()
	print("The sum of prime no is : ",str3)
	r2.close()





else: #C RECIEVING FROM P  VIA PIPE1
	os.close(w1)
	r1=os.fdopen(r1)
	str2=r1.read()
	r1.close()
	
	listofnum=sumofprime(str2)
	
	#C TO P VIA PIPE2
	os.close(r2)
	w2=os.fdopen(w2,'w')
	w2.write(listofnum)
	w2.close()
	
	
