echo "Enter th number N"
read n
k=2
echo "the list of non prime number upto N are $k  "
k=$((k+1))
while [ $k -le $n ]
do
	a=$k
	i=2
	flag=0
	while [ $i -lt $a ]
	do	
		if [ $((a%i)) == 0 ]
		then
			flag=1
			break
		fi
		i=$((i+1))
	done
	if [ $flag == 0 ]
	then 
		echo "$a"
	fi
	k=$((k+1))
done

	
	 
	
