echo "Enter the number N"
read n
a=0
b=1
i=2
c=0
echo "The non-Fibonacci series is "
while [ $i -le $n ]
do
	c=$((a+b))
	k=$((b+1))
	while [ $k -lt $c ]
	do
		echo "$k"
		k=$((k+1))
	done
	a=$b
	b=$c
	i=$((i+1))
done

