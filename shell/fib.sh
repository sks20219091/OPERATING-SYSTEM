echo "Enter the number of elements in fibonaaci series"
read n
a=0
b=1
c=0
echo $a
echo $b
i=2
while [ $i -le $n ]
do
	c=$((a+b))
	echo $c
	a=$b
	b=$c
	i=$((i+1))
done

