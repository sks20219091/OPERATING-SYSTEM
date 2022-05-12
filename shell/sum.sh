echo "Enter the number of elements :"
read n
i=1
sum=0
while [ $i -le $n ]
do
	echo "Enter the elements $i :  "
	read x
	sum=$((sum+x))
	i=$((i+1))
done
echo "The sum of element is $sum "
