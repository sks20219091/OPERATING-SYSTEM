echo "Enter the number N : "
read n
i=0
sum=0
x=0
while [ $n -gt 0 ]
do
	x=$((n%10))
	sum=$((sum+x))
	n=$((n/10))
done
echo "The sum of digits $n is $sum "

