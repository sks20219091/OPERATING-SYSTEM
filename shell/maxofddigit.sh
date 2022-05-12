echo "Enter the number N"
read n
i=0
max=$((n%10))
n=$((n/10))
while [ $n -gt 0 ]
do 
	x=$((n%10))
	if [ $x -gt $max ]
	then
		max=$x
	fi
	n=$((n/10))
done
echo "The answer is $max "
	
