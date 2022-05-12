echo "Enter the number N"
read n
sum=0
x=0
i=0
while [ $n -gt 0 ]
do
	x=$((n%10))
	sum=$((x+sum*10))
	n=$((n/10))
done
echo "The reverse number is $sum "
