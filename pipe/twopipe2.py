import os

r1,w1=os.pipe() #P TO C
r2,w2=os.pipe() #C TO P

pid=os.fork()

def extractprime(string):
	listofnumbers=string.split()
	i=0
	str3=""
	while i<len(listofnumbers):
		k=2
		n=int(listofnumbers[i])
		check=False
		while k<n:
			if n%k==0:
				check=True
				break
			k=k+1
		if check==False:
			str3=str3+" "+str(n)
		i=i+1
	return str3
		

if pid>0:
	#P TO C
	os.close(r1)
	w1=os.fdopen(w1,'w')
	n=int(input("Enter the number of elements :"))
	i=0
	str1=""
	while i<n:
		x=int(input("Enter the elements :"))
		str1=str1+" "+str(x)
		i=i+1
	w1.write(str1)
	w1.close()
	
	#recieved from child to parent via pipe2
	os.close(w2)
	r2=os.fdopen(r2)
	str=r2.read()
	print("The prime numbers are : ",str)
	
	
	
	
else:
	os.close(w1)
	r1=os.fdopen(r1)
	str2=r1.read()
	print("The elements are ",str2)
	r1.close()
	
	listofnumbers=extractprime(str2)

	#sending back to parent to child via pipe 2 
	os.close(r2)
	w2=os.fdopen(w2,'w')
	w2.write(listofnumbers)
	w2.close()
