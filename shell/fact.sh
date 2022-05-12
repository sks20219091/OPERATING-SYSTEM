echo "Enter the number N"
read n
i=1
ans=1
while [ $i -le $n ]
do
	ans=$((ans*i))
	i=$((i+1))
	
done
echo "The factorial of $n is $ans "
