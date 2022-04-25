import os , sys
import time
import string

r,w =os.pipe()
r1,w1 =os.pipe()
pid1=os.fork()

if pid1:
        print "parent"
        os.close(r)
	os.close(w1)
        w=os.fdopen(w,'w')
        print "parent is writing"
	str1=raw_input("Enter the String:")
        w.write(str1)
        w.close()
	time.sleep(2)
	print "parent is reading"
	r1=os.fdopen(r1)
	str2=r1.read()
	print str1,str2
	r1.close()
        sys.exit(0)

else:
        time.sleep(5)
        print("\nchild")
        os.close(w)
	os.close(r1)
        r=os.fdopen(r)
        print("child is reading")
        str1=r.read()
        print "Original string is:", str1
	rev_str1 = str1[::-1]
	if rev_str1 == str1:
		result=" is Palindrome" +' '
	else:
		result=" is not Palindrome"+' '
	r.close()
	w1=os.fdopen(w1,'w')
	print "child is writing"
	w1.write(result)
	w1.close()
        sys.exit(0)
