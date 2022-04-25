import os , sys

num=""
result=[]
n=input("Enter no of numbers:")
for i in range(n):
	n=input("Enter number:")
      	num=num+ str(n) +" "

r,w =os.pipe()
pid1=os.fork()
if pid1:
	print "parent"
	os.close(r)
	w=os.fdopen(w,'w')
        w.write(num)
	w.close()
	sys.exit(0)

else:
	print("\nchild")
	os.close(w)
	r=os.fdopen(r)
	s=r.read()
	l=s.split()
	for x in l:
		y=int(x)
		result.append(y)

	result.sort()
	print 'Sorted numbers are:'
	print result
	r.close()
	sys.exit(0)

	
