import os

r1,w1=os.pipe()
r2,w2=os.pipe()

pid=os.fork()
pid1=os.fork()

if pid>0 and pid1>0:
	#parent is closing read option for pipe1 & pipe2
	os.close(r1)
	os.close(r2)
	
	n=int(input("Enter the number N of elements "))
	i=0
	str1=""
	while i<n:
		x=int(input("Enter the element : "))
		str1=str1+" "+str(x)
		i=i+1
	#parent sending to child 1
	w1=os.fdopen(w1,'w')
	w1.write(str1)
	w1.close()
	
	#parent sending to child 2
	w2=os.fdopen(w2,'w')
	w2.write(str1)
	w2.close()
else:
	#child1 recieved from parent
	os.close(w1)
	r1=os.fdopen(r1)
	str2=r1.read()
	
	even=[]
	numlist=str2.split()
	en=len(numlist)
	i=0
	while i<en:
		curr=int(numlist[i])
		if(curr%2==0):
			even.append(curr)
		i=i+1
	
	if len(even)>0:
		print("The Even numbers are ",even)
	r1.close()
	
	
	os.close(w2)
	r2=os.fdopen(r2)
	str3=r2.read()
	
	odd=[]
	numlist1=str3.split()
	od=len(numlist1)
	i=0
	while i<od:
		curro=int(numlist1[i])
		if(curro%2!=0):
			odd.append(curro)
		i=i+1
	if len(odd)>0:
		print("The odd numbers are ",odd)
	r2.close()
	

		
	
	
	

