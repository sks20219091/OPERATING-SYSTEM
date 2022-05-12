import os
import random 

r,w=os.pipe()

pid=os.fork()

if pid>0:
#parent is sending the no
	print("The parents is sending the no.")
	os.close(r)
	w=os.fdopen(w,'w')
#taking the input
	n=int(input("Enter the number of terms : "))
	tosend=""
	i=0
	while i<n:
		x=int(input("Enter the terms "))
		tosend=tosend+" "+str(x)
		i=i+1
	#taking input done
	w.write(tosend)
	w.close()
else:
	print(" child is recieving the numbers")
	os.close(w)
	r=os.fdopen(r)
	str=r.read()
	print("parents has recievred the numbers ",str)
	r.close()
	

	
