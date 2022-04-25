#!/bin/bash
read -p "Enter the String: " string
if [[ $(rev <<< $string) == $string ]]
then
	echo "$string is a Palindrome"
else
	echo "$string is not a palindrome"
fi
