echo "Enter the number N"
read n
i=0
sum=0
x=0
while [ $n -gt 0 ]
do
	x=$((n%10))
	x=$((x*x*x))
	sum=$((sum+x))
	n=$((n/10))
	i=$((i+1))
done
echo "The answer is $sum "
	
