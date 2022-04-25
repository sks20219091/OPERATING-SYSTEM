import os ,sys
import time

print("The child will write number to pipe and")
print("the parent will read the number written by the child")

r, w =os.pipe()
processid = os.fork()
if processid!=0:
        print("parent")
        os.close(r)
        r=os.fdopen(w,'w')
        print("parent is waiting")
        num=raw_input("Enter the number:")
        r.write(num)
	r=os.fdopen(r)
	str=r.read()
	print str
	
        r.close()
       # sys.exit(0)

else:
        time.sleep(5)
        print("\nchild")
       # os.close(w)
        w=os.fdopen(r)
        print("child is reading")
        num=int(w.read())
        print(num)
	os.close(r)
	w=os.fdopen(w,'w')
        if num%2 == 0:
                w.write(4)
        else:
                w.write(6)
        w.close()
        sys.exit(0)

