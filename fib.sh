#!/bin/sh
                echo "Enter number of terms : "
read n
                a=0
b=1
echo "The Fibonacci series for is : "
echo $a
echo $b
i=1
while [ $i -le `expr $n - 2` ]
do
	c=`expr $a + $b`
	echo $c
	a=$b
	b=$c
	i=`expr $i + 1`
done
