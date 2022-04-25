#!/bin/bash
read -p "Enter the main string: " mainstring
read -p "Enter the substring: " substring
if [[ $mainstring =~ $substring ]]
then
	echo "$substring is present"
else
	echo "$substring is not present"
fi
