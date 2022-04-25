#!/bin/bash
read -p "Enter the string:" string
for i in $string
do
	echo $i
done | sort
