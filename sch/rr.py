def sjf(process):
	return process[1]
def main():
	numProcess=int(input("Enter the number of processes : "))
	#processList=[["P","AT","BT","WT","CT","TAT"]]
	processList=[]
	i=0
	while i<numProcess:
		arrivalTime=int(input("Enter the arival time of process %d : "%(i+1)))
		burstTime=int(input("Enter the burst time of process %d : "%(i+1)))
	
		currentList=[arrivalTime,burstTime,burstTime] #second burstTIME WILL ACT AS REMAINING TIME
		processList.append(currentList)
		i=i+1
		print("---------------------------------------------------")


	#READ THE QUANTUM :
	q=int(input("Enter the quantum time in ns : "))
	readyQ=[]
	i=0
	while i<numProcess:
		readyQ.append(processList[i])
		i=i+1

	time=0

	
	while readyQ:
		current=readyQ.pop(0)

		if current[2]<=q: #process can be finished this time
			endTime=time+current[2]
			time=time+current[2]
			waitingTime=endTime-current[0]-current[1]
			completionTime=endTime #for current one
			
			turnaroundtime=completionTime-current[0]

			index=processList.index(current)
			current.append(waitingTime)
			current.append(completionTime)
			current.append(turnaroundtime)
			processList[index]=current

		else:	
			endTime=time+q
			time=time+q
			current[2]=current[2]-q
			readyQ.append(current)

	k=0
	while k<numProcess:
		processList[k].pop(2)
		processList[k].insert(0,k+1)
		k=k+1

	#adding headers
	processList.insert(0,["P","AT","BT","WT","CT","TAT"])

	#print the table
	j=0
	#print(processList)
	while j<=numProcess:
		curr=processList[j]
		k=0
		print(str(processList[j][k])+"\t\t\t"+str(processList[j][k+1])+"\t\t\t"+str(processList[j][k+2])+"\t\t\t"+str(processList[j][k+3])+"\t\t\t"+str(processList[j][k+4])+"\t\t\t"+str(processList[j][k+5]))
		#print()
		j=j+1

	#calculating average waiting and tat time
	avgwt=0
	avgtat=0
	j=1
	while j<=numProcess:
		avgwt=avgwt+processList[j][3]
		avgtat=avgtat+processList[j][5]
		j=j+1
	print("The average waiting time is "+str(float(avgwt/float(numProcess))))
	print("\n")
	print("The average turnaround time is "+str(float(avgtat/float(numProcess))))


main()
