import os
import math

r1,w1=os.pipe()
r2,w2=os.pipe()

pid=os.fork()

def fact(n):
	i=1
	ans=1
	while i<=n:
		ans=ans*i
		i=i+1
	return ans

def npr(n,r):
	answer=fact(n)/(fact(n-r))
	return answer

def ncr(n,r):
	answer=fact(n)/(fact(n-r)*fact(r))
	return answer

def result(string):
	listofnum=str2.split()
	numn=int(listofnum[0])
	numr=int(listofnum[1])
	nprans=npr(numn,numr)
	ncrans=ncr(numn,numr)
	
	str3=str(nprans)+" "+str(ncrans)
	return str3
	
	

if pid: #P TO C VIA PIPE1
	os.close(r1)
	w1=os.fdopen(w1,'w')
	n=int(input("Enter the number N "))
	r=int(input("Enter the number R"))
	str1=str(n)+" "+str(r)
	w1.write(str1)
	w1.close()
	
	#p recieving from c via pipe2
	os.close(w2)
	r2=os.fdopen(r2)
	str2=r2.read()
	print("The N p r & N c r  is ",str2)
	r2.close()
	
	


else:	#c recieving from p via p
	os.close(w1)
	r1=os.fdopen(r1)
	str2=r1.read()
	r1.close()
	
	answer=result(str2)
	
	#c to p via pipe2
	os.close(r2)
	w2=os.fdopen(w2,'w')
	w2.write(answer)
	w2.close()
	
	
