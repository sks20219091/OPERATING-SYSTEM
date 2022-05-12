import os

r1,w1=os.pipe()
r2,w2=os.pipe()

pid=os.fork()

def ispalindrome(string):
	i=0
	j=len(string)-1
	while i<=j:
		if string[i]!=string[j]:
			return False
		i=i+1
		j=j-1
	return True

if pid>0:
	os.close(r2)
	w2=os.fdopen(w2,'w')
	print("parent is sending the string to the child")
	test=input("Enter the string to check :")
	w2.write(test)
	w2.close()
	
	#parent recieving from child from pipe 
	os.close(w1)
	r1=os.fdopen(r1)
	print("The parent is recieing from child")
	str2=r1.read()
	print("The parent recieved from the child ")
	print(str2)
	
	
	
	
	
else:
	os.close(w2)
	r2=os.fdopen(r2)
	print("child is recieving from the parent")
	str1=r2.read()
	print("Child recieved from parent",str1)
	r2.close()
	
	ans=ispalindrome(str1)
	result=""
	
	if ans==True:
		result="The string is palindrome"
	else:
		result="the string is not a palindrome"
	
	
	#child is sending the result back to parent
	os.close(r1)
	w1=os.fdopen(w1,'w')
	print("child is sending to the parent")
	w1.write(result)
	print("child sent to the parent")
	w1.close()
	
	
	
	
	
