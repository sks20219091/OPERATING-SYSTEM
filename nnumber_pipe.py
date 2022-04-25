#Transferring n numbers from parent process to child process
import os , sys
import time

num=""
n=input("Enter no of numbers:")
r,w =os.pipe()
pid1=os.fork()
if pid1:
	print "parent"
	os.close(r)
	w=os.fdopen(w,'w')
	print "parent is writing"
	for i in range(n):
	        n=input("Enter number:")
        	num=num+ str(n) +" "
	w.write(num)
	w.close()
	sys.exit(0)

else:
	time.sleep(5)
	print("\nchild")
	os.close(w)
	r=os.fdopen(r)
	print("child is reading")
	str=r.read()
	print "number is:", str
	r.close()
	sys.exit(0)
