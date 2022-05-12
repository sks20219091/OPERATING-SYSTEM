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
	
		currentList=[arrivalTime,burstTime]
		processList.append(currentList)
		i=i+1
		print("---------------------------------------------------")
	waitingTime=0
	completionTime=0

	i=1

	readyQ=[processList[0]] #first item in ready queue
	wait=0
	burst=0
	j=1
	i=0
	while readyQ:
		current=readyQ.pop(0)
		endTime=burst+current[1]#process goes on till this time
		j=0
		#check for all those which have arrived till now
		while j<numProcess:
			local=processList[j]
			if local[0]>current[0] and local[0]<=endTime and readyQ.count(local)==0 and len(local)==2:
				readyQ.append(local)
			elif local[0]>endTime:
				break
			j=j+1

		#we have ready q now
		readyQ.sort(key=sjf)
	
		completionTime=endTime #for current one
		waitingTime=completionTime-current[0]-current[1]
		turnaroundtime=completionTime-current[0]
	
		#update the clock
		burst=endTime
	
		index=processList.index(current)
		current.append(waitingTime)
		current.append(completionTime)
		current.append(turnaroundtime)
		processList[index]=current


	#append process number to eac process
	k=0
	while k<numProcess:
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
