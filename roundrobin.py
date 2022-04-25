process=[]
n=input("Enter no of process: ")
q=input("Enter time quantum: ")
ctime=0
tat=0
wt=0
for i in range(n):
	process.append([])
	process[i].append(raw_input("Enter pid: "))
	process[i].append(input("Enter arrival time: "))
	process[i].append(input("Enter burst time: "))
	process[i].append(process[i][2])
	process[i].append(ctime)
	process[i].append(tat)
	process[i].append(wt)
	print ''

process.sort(key = lambda process:process[1])
t=0
while(1):
	done=1
	for i in range(n):
		if(process[i][3]>0):
			if(process[i][3]>q):
				process[i][3]-=q
				t+=q
				done=0
			else:
				t+=process[i][3]
				process[i][3]=0
				process[i][4]=t
				process[i][5]=t- process[i][1]
				process[i][6]=process[i][5]-process[i][2]
	if(done==1):
		break

print 'PID\tAT\tBT\tCT\tTAT\tWT'
for i in range(n):
	print process[i][0],'\t',process[i][1],'\t',process[i][2],'\t',process[i][4],'\t',process[i][5],'\t',process[i][6]
