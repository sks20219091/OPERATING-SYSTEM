#!/bin/bash
echo -n "Enter number:"
read NUM
Q=`expr $NUM % 2`
if [[ $Q == 0 ]]
then
	echo "The $NUM is even"
else
	echo "The $NUM is odd"
fi 
