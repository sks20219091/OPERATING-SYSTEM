echo "Enter the number of elements :"
read n
arr=()
i=0
while [[ $i -lt $n ]]
do
	read x
	arr+=($x)
	i=$((i+1))
done
i=0
k=0
while [[ $i -lt $n ]]
do	
	j=$i
	while [[ $j -le $n ]]
	do
		curr=${arr[$j]}
		if [[ $curr -le ${arr[i]} ]]
		then
			temp=${arr[i]}
			arr[$i]=${arr[$j]}
			arr[$j]=$temp
		fi
		j=$((j+1))
	done
	i=$((i+1))
done

echo "The sorted array is "${arr[*]}
echo "first element of array is "${arr[1]}
#len=$((n-1))
echo "The last element of array is "${arr[$n]}	
