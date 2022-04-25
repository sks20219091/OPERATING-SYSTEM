process=[]
n=input("Enter no of process: ")
for i in range(n):
	process.append([])
	process[i].append(raw_input("Enter pid: "))
	process[i].append(input("Enter arrival time: "))
	process[i].append(input("Enter burst time: "))
	print ' '
process.sort(key = lambda process:process[1])

ctime=process[0][1]
print 'pid\tat\tbt\tct\ttat\twt'
for i in range(n):
	ctime+=process[i][2]
	tat=ctime-process[i][1]
	wt=tat-process[i][2]
	print process[i][0],'\t',process[i][1],'\t',process[i][2],'\t',ctime,'\t',tat,'\t',wt
