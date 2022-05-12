OTP=12345
import os

import math

r1,w1=os.pipe()
r2,w2=os.pipe()

pid=os.fork()

'''def sumofprime(string):
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
'''		
	

if pid>0: 
	#P TO C VIA PIPE1
	os.close(r1)
	w1=os.fdopen(w1,'w')
	str1=int(input("Enter the OTP "))
	num=str(str1)
	w1.write(num)
	w1.close()
	
	#p recieving from c via pipe2
	os.close(w2)
	r2=os.fdopen(r2)
	str3=r2.read()
	print(str3)
	r2.close()





else: #C RECIEVING FROM P  VIA PIPE1
	os.close(w1)
	r1=os.fdopen(r1)
	
	str2=r1.read()
	print("The transaction OTP is ",OTP)
	r1.close()
	
	ans=""
	x=int(str2)
	if x==OTP:
		ans="TRANSACTION IS SUCCESFUL"
	else:
		ans="INVALID OTP "
	
	#C TO P VIA PIPE2
	os.close(r2)
	w2=os.fdopen(w2,'w')
	w2.write(ans)
	w2.close()
	
	
