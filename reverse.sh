#!/bin/bash
read -p "Enter Number: " N
result=0
while [[ $N -gt 0 ]]
do
	r=`expr $N % 10`
	result=`expr $result \* 10`
	result=`expr $result + $r`
	N=`expr $N / 10`
done
echo $result
