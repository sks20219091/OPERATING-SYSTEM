import os , sys
import time
import string

num=""
prime=[]
result=""
n=input("Enter no of numbers:")
r,w =os.pipe()
r1,w1 =os.pipe()
pid1=os.fork()
if pid1:
        print "parent"
        os.close(r)
	os.close(w1)
        w=os.fdopen(w,'w')
        print "parent is writing"' '.join(str(x) for x in result)
        for i in range(n):
                n=input("Enter number:")
                num=num+ str(n) +" "
        w.write(num)
        w.close()
	time.sleep(2)
	print "parent is reading"
	r1=os.fdopen(r1)
	str1=r1.read()
	print str1
	r1.close()
        sys.exit(0)

else:
        time.sleep(10)
        print("\nchild")
        os.close(w)
	os.close(r1)
        r=os.fdopen(r)
        print("child is reading")
        str1=r.read()
        print "number is:", str1
	l=str1.split()
	for x in l:
		y=int(x)
		prime.append(y)
	
	for i in range(len(prime)):
		flag=0
		for j in range(2,prime[i]):
			if prime[i] % j ==0:
				flag=1
				break
		if flag==0:
			result=result+ str(prime[i])+' '
	r.close()
	w1=os.fdopen(w1,'w')
	print "child is writing"
	w1.write(result)
	w1.close()
        sys.exit(0)

