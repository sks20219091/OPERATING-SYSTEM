import os
import random

r,w=os.pipe()

pid=os.fork()

if pid>0:
#parent is sending to the child
	print("parent is sending the numbers")
	os.close(r)
	w=os.fdopen(w,'w')
#taking the input
	n=int(input("Enter the number of terms :  "))
	i=0
	tosend=""
	while i<n:
		x=int(input("enter the elemem=nts: "))
		tosend=tosend+" "+str(x)
		i=i+1
	w.write(tosend)
	print("parent has sent to the child")
	w.close()
else:
	print("child will be recieving the numbers ")
	os.close(w)
	r=os.fdopen(r)
	str=r.read()
	print("child has recieved the numbers : ",str)
	r.close()

	
	
