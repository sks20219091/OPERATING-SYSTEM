#!/bin/bash
read -p "Enter number: " num
a=1
fact=1
while [ $a -le $num ]
do
	fact=`expr $fact \* $a`
	a=`expr $a + 1`
done
echo "Factorial of $num is : $fact"
