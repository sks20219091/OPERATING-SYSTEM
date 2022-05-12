def main():
	numProcess=int(input("Enter the number of processes : "))
	processList=[["P","AT","BT","WT","CT","TAT"]]
	i=0
	while i<numProcess:
		arrivalTime=int(input("Enter the arival time of process %d : "%(i+1)))
		burstTime=int(input("Enter the burst time of process %d : "%(i+1)))
	
		currentList=[i+1,arrivalTime,burstTime]
		processList.append(currentList)
		i=i+1
		print("---------------------------------------------------")
	waitingTime=0
	completionTime=0

	i=1

	while i<=numProcess:
		currentProcess=processList[i]
		currentProcess.append(waitingTime-currentProcess[1])
		completionTime=completionTime+currentProcess[2]
		currentProcess.append(completionTime)
		currentProcess.append(currentProcess[4]-currentProcess[1])
		#now change the waiting time and totalTime till now
		waitingTime=waitingTime+currentProcess[2]
		i=i+1

	print(processList)
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
