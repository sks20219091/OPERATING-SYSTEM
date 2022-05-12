import os

r1,w1=os.pipe() #C TO P 
r2,w2=os.pipe() #P TO C

pid = os.fork()
def ispalindrome(string):
	i=0
	j=len(string)-1
	while i<=j:
		if string[i] != string[j]:
			return False
		i=i+1
		j=j-1
	return True
	
if pid>0:
	#PARENT HAS SEND THE STRING TO THE CHILD
	os.close(r2)
	w2=os.fdopen(w2,'w')
	str1=input("enter the string to be checked")
	print("parents is sending the string to child ")
	w2.write(str1)
	w2.close()
	print("Parent has sent string to the child")
	
	#Received from the pipe1
	os.close(w1)
	print("parent will recieved from the child")
	r1=os.fdopen(r1)
	str2=r1.read()
	print("parent has recieved from the child")
	print(str2)
	
else:
	os.close(w2)
	r2=os.fdopen(r2)
	test=r2.read()
	print("string recieved from parent ",test)
	r2.close()
	#checking palindrome
	answer=ispalindrome(test)
	result=""
	if answer==True:
		result="the given string is palindrome"
	else:
		result="the given string is not palindrome"
	#child sending to  parent
	os.close(r1)
	print("child sending  response to the parent")
	w1=os.fdopen(w1,'w')
	w1.write(result)
	print("Child has sent response to the parent")
	w1.close()
	
	
	
