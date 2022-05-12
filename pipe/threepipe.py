import os

r,w=os.pipe()
r1,w1=os.pipe()

pid=os.fork()
pid1=os.fork()

if pid>0 and pid1>0:
    os.close(r)
    os.close(r1)
    
    
    n=int(input("Enter number of input : "))
    send=""
    for i in range(0,n):
        x=int(input("Enter the number :"))
        send=send+" "+str(x)
    w=os.fdopen(w,'w')
    
    w.write(send)
    print("The parent has sent to Child 1st")
    w.close()


    w1=os.fdopen(w1,'w')
    w1.write(send)
    print("The parent has sent to Child 2nd")
    w1.close()

else:
    os.close(w)
    r=os.fdopen(r)
   
    str1=r.read()
    print("The  Child 1st has received string")
    
   
    list=str1.split()
    even=[]
    
    for i in range(0,len(list)):
        cur=int(list[i])
        if cur%2==0:
            even.append(cur)
    
    r.close()
    if len(even)>0:
        print("Child 1st is printing Even",even)
    


   
    os.close(w1)
    r1=os.fdopen(r1)
    str1=r1.read()
    print("The  Child 2nd has received string")
   
    list=str1.split()
   
    odd=[]
    for i in range(0,len(list)):
        cur=int(list[i])
        if cur%2!=0:
            odd.append(cur)
        
    r1.close()
    
    
    if len(odd)>0:
        print("Child 2nd is printing Odd",odd)
