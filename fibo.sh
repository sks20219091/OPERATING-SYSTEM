#!/bin/bash
read -p "Enter the no of terms: " n
a=0
b=1
sum=0
i=0
echo -n $a $b
while [[ $i -lt `expr $n - 2` ]]
do
	sum=`expr $a + $b`
	echo -n " $sum"
	a=$b
	b=$sum
	i=`expr $i + 1`
done
echo " "
