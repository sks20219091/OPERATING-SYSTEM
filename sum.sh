#!/bin/bash
echo -n "Enter no of numbers:"
read NUM
sum=0
a=0
while [[ $a -le $NUM ]]
do
	sum=`expr $a + $sum`
	a=`expr $a + 1`
done
echo "Sum of $NUM is : $sum"
