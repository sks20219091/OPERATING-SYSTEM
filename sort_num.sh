#!/bin/bash
read -p "Enter the numbers" num
for i in $num 
do
	echo $i
done | sort -g
